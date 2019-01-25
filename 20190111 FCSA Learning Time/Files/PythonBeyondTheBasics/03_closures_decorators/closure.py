def outer(x, z):
    def inner(y):
        return x + y + z
    return inner

i = outer(6, 1)

print(i(2))
print(i(5))

print(i.__closure__)


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

sqr = raise_to(2)
print(sqr(4))
print(sqr(10))


message = 'global'
def enclosing():
    # message = 'enclosing'

    def local():
        # global message
        nonlocal message
        message = "local"

    print(f'enclosing message: {message}')
    local()
    print(f'enclosing message: {message}')

print(f'enclosing message: {message}')
enclosing()
print(f'enclosing message: {message}')

