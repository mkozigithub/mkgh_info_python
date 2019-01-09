
class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @staticmethod
    def static_hello():
        print(f"Hello from ShippingContainer")

    # use @staticmethod when a reference to the class is not needed
    # @staticmethod
    # def _get_next_serial():
    #     result = ShippingContainer.next_serial
    #     ShippingContainer.next_serial += 1
    #     return result

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

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)


    def __init__(self, owner_code, length_ft, contents):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        # self.serial = ShippingContainer.next_serial
        # ShippingContainer.next_serial += 1
        self.serial = ShippingContainer._get_next_serial()

    @property
    def volume_ft3(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT = 100

    @staticmethod
    def static_hello():
        print("hello from RefrigeratedShippingContainer")

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit -32) * 5/9

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        # if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
        #     raise ValueError("Temp too hot!")
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temp too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    @property
    def volume_ft3(self):
        return super().volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT

class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    @RefrigeratedShippingContainer.celsius.setter
    def celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Too cold!")
        RefrigeratedShippingContainer.celsius.fset(self, value)
        # if not (HeatedRefrigeratedShippingContainer.MIN_CELSIUS <= value <= RefrigeratedShippingContainer.MAX_CELSIUS):
        #     raise ValueError('Temp is out of range!')
        # self.celsius = value


if __name__ == "__main__":
    c1 = ShippingContainer('YML', 10, 'books')
    print(c1, c1.serial, c1.owner_code, c1.contents)
    c2 = ShippingContainer('MAE', 11, 'clothes')
    print(c2, c2.serial, c2.owner_code, c2.contents)
    print(ShippingContainer.next_serial, c2.next_serial)

    c3 = ShippingContainer.create_empty('EMC', 12)
    print(c3, c3.serial, c3.owner_code, c3.contents)

    c4 = ShippingContainer.create_with_items('ABC', 13, range(1, 5))
    print(c4, c4.serial, c4.owner_code, c4.contents)

    ShippingContainer.static_hello()
    RefrigeratedShippingContainer.static_hello()
    sc1 = ShippingContainer('ab', 14, "electronics")
    sc1.static_hello()
    rsc1 = RefrigeratedShippingContainer('cd', 14.5, 'food', 3)
    rsc1.static_hello()

    sc2 = ShippingContainer.create_empty("ef", 15)
    print(sc2)
    sc2.static_hello()
    rsc2 = RefrigeratedShippingContainer.create_empty('gh', 16, celsius=1)
    print(rsc2)
    rsc2.static_hello()

    rsc3 = RefrigeratedShippingContainer('yz', 17, "pineapples", 3)
    print(vars(rsc3))

    rsc3 = RefrigeratedShippingContainer.create_empty('xy', length_ft=18, celsius=1.5)
    # rsc3.celsius = 12 # property celsius raises error when max exceeded
    rsc3.celsius = 2.5
    rsc3.fahrenheit = 39
    print(vars(rsc3))
    print(rsc3.celsius, rsc3.fahrenheit, rsc3.volume_ft3)

    hrsc1 = HeatedRefrigeratedShippingContainer("YML", length_ft=40, contents="yams", celsius=-18)
    print(hrsc1.celsius, hrsc1.fahrenheit, hrsc1.volume_ft3)
    # hrsc1.celsius = 25 # raises error
    # hrsc1.fahrenheit = -14 # raises error
    hrsc2 = HeatedRefrigeratedShippingContainer.create_empty('YML', length_ft=40, celsius=4.0)
