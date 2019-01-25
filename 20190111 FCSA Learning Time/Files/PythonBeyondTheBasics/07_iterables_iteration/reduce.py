# reduce repeatedly applies a function to elements of a sequence, reducing them to a single value

from functools import reduce
import operator

sum = reduce(operator.add, [1, 2, 3, 4, 5])
print(sum)

# functionally equivalent to:
numbers = [1, 2, 3, 4, 5]
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[:2]:
    accumulator = operator.add(accumulator, item)
print(accumulator)


def mul(x, y):
    print(f'mul {x} {y}')
    return x * y
result = reduce(mul, range(1,10))
print(result)

# reduce(mul, []) # empty list raises exception
print(reduce(mul, [1])) # list with one element returns element without running function


# optional initial value
values = [1, 2, 3]
print(reduce(operator.add, values, 0))
values = []
print(reduce(operator.add, values, 0))  # when optional initializer is supplied, empty list argument doesn't raise exception