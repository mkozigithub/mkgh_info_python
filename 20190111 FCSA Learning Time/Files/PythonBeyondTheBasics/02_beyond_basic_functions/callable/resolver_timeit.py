from timeit import timeit
from resolver import Resolver

r = Resolver()
t = timeit(setup="from __main__ import r", stmt = "r('python.org')", number = 1)
print(f"Initial time: {t:f}")

t = timeit(setup="from __main__ import r", stmt = "r('python.org')", number = 1)
print(f"Second time: {t:f}")

