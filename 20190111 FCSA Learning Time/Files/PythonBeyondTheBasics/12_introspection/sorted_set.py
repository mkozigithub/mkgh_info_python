# Abstract base classes for Containsers: https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence, Set

from bisect import bisect_left
from itertools import chain

class SortedSet(Sequence, Set):
    
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    # satisfies the container protocol
    def __contains__(self, item):
        index = bisect_left(self._items, item)
        return (index != len(self._items)) and (self._items[index] == item)

    # satisfies the sized protocol
    def __len__(self):
        return len(self._items)

    # satisfies the iterable protocol
    def __iter__(self):
        return iter(self._items)

    # satisfies sequence indexing protocol
    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    # satisfies repr protocol
    def __repr__(self):
        val = repr(self._items) if self._items else ''
        return f"SortedSet({val})"

    # override equality functionality inherited form object
    # default is to test for reference equality (like x is y)
    # satisfies equality protocol
    def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    # part of equality protocol
    def __ne__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    def count(self, item):
        return int(item in self)

    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items) and (self._items[index] == item)):
            return index
        raise ValueError(f'{item} not found.')

    # sequence protocol for concatenation
    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

    # sequence protocol for repitition
    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    # sequence protocol for repitition
    def __rmul__(self, lhs):
        return self * lhs

    # set protocol - named function based on inherited functionality from Set
    def issubset(self, Iterable):
        return self <= SortedSet(Iterable)

    # set protocol - named function based on inherited functionality from Set
    def issuperset(self, Iterable):
        return self >= SortedSet(Iterable)

    # set protocol - named function based on inherited functionality from Set
    def intersection(self, Iterable):
        return self & SortedSet(Iterable)

    # set protocol - named function based on inherited functionality from Set
    def union(self, Iterable):
        return self | SortedSet(Iterable)

    # set protocol - named function based on inherited functionality from Set
    def symmetric_difference(self, Iterable):
        return self ^ SortedSet(Iterable)

    # set protocol - named function based on inherited functionality from Set
    def difference(self, Iterable):
        return self - SortedSet(Iterable)



if __name__ == "__main__":
    from random import randrange

    s = SortedSet(randrange(1000) for _ in range(2000))
    print(len(s))

    from timeit import timeit

    t = timeit(setup="from __main__ import s", 
            stmt="[s.count(i) for i in range(1000)]",
            number=100)
    print(t)


    # checking if protocols are implemented
    from collections.abc import *
    print(issubclass(list, Sequence))
    print(issubclass(list, Sized))
    print(issubclass(dict, Mapping))
    print(issubclass(dict, Sized))
    print(issubclass(dict, Iterable))
