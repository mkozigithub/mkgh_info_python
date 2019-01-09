import functools

def check_non_negative(index):
    def validator(f):
        @functools.wraps(f)
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(f'Argument {index} must be non-negative.')
            return f(*args)
        return wrap
    return validator

@check_non_negative(1)
def create_list(value, size):
    """Creates a list of value that is size in length"""
    return [value] * size

print(create_list('a', 3))
# print(create_list(123, -6)) # throws exception
print(help(create_list))
