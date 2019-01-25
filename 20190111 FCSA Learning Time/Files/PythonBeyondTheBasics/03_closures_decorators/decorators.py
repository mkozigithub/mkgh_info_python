def vegetable():
    return 'blomkal'

def animal():
    return 'bjorn'

def mineral():
    return 'stal'

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


def full_block():
    return u'This is a full block: \u2588'

@escape_unicode
def full_block2():
    return u'This is a full block: \u2588'

print(full_block())
print(full_block2())


class CallCount:
    def __init__(self, f):
        self.f =  f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

# class used as decorator, function passed into __init__
@CallCount
def hello(name):
    print(f"Hello, {name}")

hello('mark')
hello('nathan')
print(f"Call Count: {hello.count}")


# class instance used as a decorator, function passed into the __call__ instance method
class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"Calling {f}")
            return f(*args, *kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

print(rotate_list)
l = [1, 2, 3]
print(l)
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)
tracer.enabled = False
l = rotate_list(l)
print(l)


# using multiple decorators
@tracer
@escape_unicode
def full_block_3(name):
    return name + u'\u2588'

tracer.enabled = True
print(full_block_3("mark"))
print(full_block_3("nathan"))


# use decorator on method
class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix

im = IslandMaker(' Island')
print(im.make_island('Python'))
print(im.make_island('Llama'))


# use functools.wraps to preserve meta data from wrapped item
import functools

def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello():
    "Print a well-known message."
    print("hello, world!")

print(help(hello))
