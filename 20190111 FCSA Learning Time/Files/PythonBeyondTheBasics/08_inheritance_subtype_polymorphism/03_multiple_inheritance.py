from simple_list import *


if __name__ == "__main__":
    # use isinstance for runtime type checking
    print(isinstance(3, int))
    print(isinstance('hello', str))
    print(isinstance(4.567, bytes))
    sl = SortedList([2,1,88,55])
    print(isinstance(sl, SimpleList), isinstance(sl, SortedList))

    # check for any matched
    x = []
    print(isinstance(x, (float, dict, list)))

    print(issubclass(IntList, SimpleList), issubclass(SortedList, SimpleList), issubclass(SimpleList, list))
