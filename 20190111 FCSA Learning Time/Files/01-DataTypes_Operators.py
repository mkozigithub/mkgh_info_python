#   integer: unlimited precision signed integer
i = 42
i = 0b10      # binary integer
i = 0o10      # octal integer
i = 0x10      # hexadecimal integer
i = int(3.5)  # convert float to int, note always rounds toward zero
i = int(-3.5)  # convert float to int, note always rounds toward zero
i = 0x10      # hexadecimal integer
i = int("496")  # convert string to int
i = int("102", 3)  # convert string to int using optional base
i = 47**200  # can be as large as machine memory allows
print(f'integer type ({type(i)}): {i}')

#   float: IEEE-754 double precision (64-bit), 53 bits of binary precision, 15 to 16 significant digits of decimal precision
f = 3.125
f = 3e8
f = 1.61e-35
f = float(7)
f = float("1.618")
f = float("nan")
f = float("inf")
f = float("-inf")

#   NoneType (like null), represents the absence of a value
n = None
print(f'integer type ({type(n)}): {n}')
test = n is None
print(f"n = None, n is None = {test}")

#   bool - either True or False
b = False
b = bool(0)         # 0 is false
b = bool(1)         # all other integers are true
b = bool(-42)       # all other integers are true
b = bool(0.0)       # 0 decimal is false
b = bool(-1.1234)   # all other floats are true
b = bool([])        # empty list is false
b = bool([6])       # non-empty list is true
b = bool("")        # empty string is false
b = bool("a")       # non-empty string is true
b = bool("False")   # is true, since not an empty string
print(f'integer type ({type(b)}): {b}')

# operators: https://www.tutorialspoint.com/python/python_basic_operators.htm

# strings
print('this is a string ("str")')   # can use single quotes (' ') or double quotes (" ") or both
print("this isn't a problem")       # use both
str1 = "one " "two " "three"
print(str1)     # adjacent strings are automatically concatenated

# multiline string
multiline = """A
multi
line
string
"""
print(multiline)
multiline = '''Can
also
use
single quotes
'''
print(multiline)

# raw strings (no escape processing)
#print('C:\Users\Bob\New') # \u is processed as unicode, raises error
print(r'C:\Users\Bob\New')  # this does not process \ as escape

# string conversions
print(str(496))
print(str(6.02e23))
print(str(True))

