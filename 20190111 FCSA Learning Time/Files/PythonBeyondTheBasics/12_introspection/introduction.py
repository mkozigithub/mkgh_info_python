i = 7
print(1, type(i))
print(2, int)
print(3, repr(int))
print(4, type(i) is int)
print(5, int(78), type(i)(78))
print(6, type(type(i)), i.__class__.__class__)
print(7, type(i) is i.__class__)
print(8, i.__class__.__class__.__class__, issubclass(type, object), type(object))
print(9, isinstance(i, int))