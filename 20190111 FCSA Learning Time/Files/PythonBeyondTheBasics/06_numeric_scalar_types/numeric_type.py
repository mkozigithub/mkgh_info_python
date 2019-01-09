from math import factorial as fac
import sys

# python ints can be verrrry large
print(sys.int_info)
print(fac(1000))

# float (base 2 number)
print(sys.float_info)
print(float(2**53))
print(float(2**53 + 1))
print(float(2**53 + 2))
print(float(2**53 + 3))
print(float(2**53 + 4))
print(0.8 - 0.7)
print(1/3)

# decimals (base 10 arithmetic)
import decimal
from decimal import Decimal
print(decimal.getcontext())
print(Decimal(5))
print(Decimal('0.8'))
print(Decimal('0.8') - Decimal('0.7'))
print(Decimal(0.8) - Decimal(0.7))

decimal.getcontext().traps[decimal.FloatOperation] = True
# print(Decimal(0.8) - Decimal(0.7))  # will raise an exception if literal float is used, so must use string numeric literal
# Decimal('0.8') > 0.7 # this also raises an exception
print(Decimal('0.8') - Decimal('0.7'))

# precision of decimals is preserved during computation
a = Decimal(3)
b = Decimal('3.0')
c = Decimal('3.00')
print(a)
print(b)
print(c)
print(a * 2)
print(b * 2)
print(c * 2)

# setting precision
decimal.getcontext().prec = 6
d = Decimal('1.234567')
print(d)
print(d + Decimal(1)) # uses precision set on getcontext()

print(Decimal('Infinity'))
print(Decimal('-Infinity'))
print(Decimal("NaN"))
print(Decimal("NaN") + Decimal("1.4124"))


# fractions for rational numbers
from fractions import Fraction
two_thirds = Fraction(2, 3)
print(two_thirds)
four_fifths = Fraction(4, 5)
print(four_fifths)
print(two_thirds + four_fifths)
print(two_thirds - four_fifths)
print(two_thirds * four_fifths)
print(two_thirds / four_fifths)
print(two_thirds // four_fifths)
print(two_thirds % four_fifths)

from math import floor, ceil
print(floor(two_thirds))
print(ceil(two_thirds))

print(Fraction(209850803495093845034))
print(Fraction(0.5))
print(Fraction(0.1))
print(Fraction('0.1'))
print(Fraction('22/7'))

# complex numbers
print(2j, type(2j))
print(3 + 4j)
print(complex(3))
print(complex(-2,3))
print(complex('-4+5j'))
c = 8 + 9j
print(c, c.real, c.imag, c.conjugate())

import cmath
print(cmath.sqrt(-1))
print(cmath.phase(1+1j), abs(1+1j))
modulus, phase = cmath.polar(4+6j)
print(modulus, phase)
print(cmath.rect(modulus, phase))

# abs - gives distance from zero
print(abs(-5), abs(-5.0), abs(Decimal(-5)), abs(Fraction(-5, 1)), abs(complex(0, -5)))

# round
print(round(0.2812, 3), round(0.625, 1))
print(round(1.5), round(2.5))  # rounding 5 goes to nearest even number
print(round(Decimal('3.25'), 1))
print(round(Fraction(57/100), 2), round(Fraction(57/100), 1), round(Fraction(57/100), 0))

# base conversions
print(0b101010, 0o52, 0x2a)
print(bin(42), oct(42), hex(42))
print(bin(42)[2:], oct(42)[2:], hex(42)[2:])

print(int("2a", base=16))
print(int("2z", base=36))

# date
import datetime
print(datetime.date(2014, 1, 6), datetime.date(year=2014, month=1, day=6))
print(datetime.date.today(), datetime.date.fromtimestamp(1000000000), datetime.date.fromordinal(720669))
d = datetime.date.today()
print(d.year, d.month, d.day, d.weekday(), d.isoweekday(), d.isoformat(), d.timetuple())
print(d.strftime('%A %d %B %Y'), f"The date is {d:%A %d %B %Y}")
print(f"{d:%A} {d:%d} {d:%B} {d.year}")
print(datetime.date.min, datetime.date.max)
print(datetime.datetime.now(), datetime.datetime.utcnow())

# time
print(datetime.time(3), datetime.time(3, 1), datetime.time(3, 1, 2), datetime.time(3, 1, 2, 232))
print(datetime.time(hour=23, minute=58, second=59, microsecond=99999))
t = datetime.datetime.now().time()
print(t.hour, t.minute, t.second, t.microsecond, t.isoformat(), t.strftime('%Hh%Mm%Ss'), f"{t.hour}h{t.minute}m{t.second}s")
print(datetime.time.min, datetime.time.max, datetime.time.resolution)

d = datetime.date.today()
t = datetime.time(8, 15)
print(datetime.datetime.combine(d,t))
print(datetime.datetime.strptime("Monday 6 January 2014, 12:13:31", "%A %d %B %Y, %H:%M:%S"))

# timedelta
td = datetime.timedelta(weeks=3, days=4, hours=11, minutes= 45, seconds= 90, milliseconds=2, microseconds=5)
print(td, td.days, td.seconds, td.microseconds, f"str: {str(td)}", f"repr: {repr(td)}")
a = datetime.datetime(year=2018, month=5, day=8, hour=14, minute=22)
b = datetime.datetime(year=2018, month=3, day=14, hour=12, minute=9)
d = a - b
print(d, d.total_seconds())
d = datetime.datetime.today() + datetime.timedelta(weeks=1) * 3
print(d)

# timezones
cet = datetime.timezone(datetime.timedelta(hours=1), "CET")
print(repr(cet))
departure = datetime.datetime(year=2018, month=4, day=28, hour=15, minute=30, tzinfo=cet)
print(repr(departure))
arrival = datetime.datetime(year=2018, month=4, day=28, hour=17, minute=5, tzinfo=datetime.timezone.utc)
print(departure, arrival, arrival-departure)
