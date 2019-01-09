from pprint import pprint as pp

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f'Calling {f}')
            return f(*args, **kwargs)
        return wrap

m = map(ord, 'The quick brown fox')
print(repr(m))
print(list(m))

result = map(Trace()(ord), 'The quick brown fox')
print(repr(result))
print(next(result))
print(next(result))

def create_tuple(a, b, c):
    return (a, b, c)
a = "ABCDEF"
b = "1234"
c = "VWXYZ"
result = map(create_tuple, a, b, c)
pp(list(result))
