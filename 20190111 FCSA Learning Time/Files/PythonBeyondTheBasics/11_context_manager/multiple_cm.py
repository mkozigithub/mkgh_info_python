# with cm1() as a, cm2() as b:
#     BODY

# is the same as

# with cm1() as a:
#     with cm2() as b:
#         BODY

import contextlib

@contextlib.contextmanager
def nest_test(name):
    print(f'Entering {name}')
    yield name
    print(f'Exiting {name}')


@contextlib.contextmanager
def propogater(name, propogate):
    try:
        yield
        print(name, 'exited normally')
    except Exception:
        print(name, 'recieved an exception')
        if propogate:
            raise


with nest_test('outer'), nest_test('inner'):
    print('BODY')

print()

with nest_test('outer'):
    with nest_test('inner'):
        print('BODY')

print()

with nest_test('outer') as n1, nest_test(f'inner, nested in {n1}'):
    print('BODY')

print()

with propogater('outer', True), propogater('inner', False):
    raise TypeError('Cannot convert lead into gold.')

print()

with propogater('outer', False), propogater('inner', True):
    raise TypeError('Cannot convert lead into gold.')

print()

with propogater('outer', True), propogater('inner', True):
    raise TypeError('Cannot convert lead into gold.')

print()

# make sure to pass a context manager
with [nest_test('a'), nest_test('b')]:  # we are actually passing a list, which is not a context manager
    print("didn't pass a context manager")

