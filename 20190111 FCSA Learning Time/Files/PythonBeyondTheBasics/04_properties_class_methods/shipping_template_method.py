
class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    # use @classmethod when a reference to the class is needed
    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    # named constructors
    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    def __init__(self, owner_code, length_ft, contents):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()

    @property
    def volume_ft3(self):
        return self._calc_volume()

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT = 100

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit -32) * 5/9

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temp too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT

class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    def _set_celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Too cold!")
        super()._set_celsius(value)


if __name__ == "__main__":
    sc1 = ShippingContainer.create_empty('sc', 40)
    print(sc1.volume_ft3)

    rsc2 = RefrigeratedShippingContainer('yz', 17, "pineapples", 3)
    # rsc2.fahrenheit = 40
    print(vars(rsc2))

    rsc3 = RefrigeratedShippingContainer.create_empty('xy', length_ft=40, celsius=1.5)
    # rsc3.celsius = 12 # property celsius raises error when max exceeded
    rsc3.celsius = 2.5
    rsc3.fahrenheit = 39
    print(vars(rsc3))
    print(rsc3.celsius, rsc3.fahrenheit, rsc3.volume_ft3)

    hrsc1 = HeatedRefrigeratedShippingContainer("YML", length_ft=40, contents="yams", celsius=-18)
    print(hrsc1.celsius, hrsc1.fahrenheit, hrsc1.volume_ft3)
    # hrsc1.celsius = 25 # raises error
    # hrsc1.celsius = -25 # raises error
    # hrsc1.fahrenheit = -14 # raises error
    # hrsc1.fahrenheit = 50 # raises error
    hrsc2 = HeatedRefrigeratedShippingContainer.create_empty('YML', length_ft=40, celsius=4.0)
