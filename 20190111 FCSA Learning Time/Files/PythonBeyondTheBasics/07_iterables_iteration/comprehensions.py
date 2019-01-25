l = [i * 2 for i in range(10)]
print(repr(l), type(l))

d = {i: i*2 for i in range(10)}
print(repr(d), type(d))

s = {i for i in range(10)}
print(repr(s), type(s))

g = (i for i in range(10))
print(repr(g), type(g))

from pprint import pprint as pp

cartesian = [(x, y) for x in range(5) for y in range(5)]
pp(cartesian)

values = [x / (x - y) for x in range(100) if x > 50 
                      for y in range(100) if x - y != 0]
pp(values)

values = [(x, y) for x in range(10) for y in range(x)]
pp(values)
# equivalent to:
values1 = []
for x in range(10):
    for y in range(x):
        values1.append((x,y))
pp(values1 == values)

nested = [[y * 3 for y in range(x)] for x in range(10)]
pp(nested)
#equivalent to:
nested1 = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y*3)
    nested1.append(inner)
print(nested == nested1)
