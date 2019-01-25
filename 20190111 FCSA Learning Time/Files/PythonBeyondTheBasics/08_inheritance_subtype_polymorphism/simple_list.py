class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(self._items)

class IntList(SimpleList):
    def __init__(self, items):
        for x in items: self.validate(x)
        super().__init__(items)

    def validate(self, item):
        IntList._validate(item)

    def add(self, item):
        self.validate(item)
        super().add(item)        

    @staticmethod
    def _validate(item):
         if not isinstance(item, int):
            raise   TypeError('IntList only supports ints.')               

    def __repr__(self):
        return "IntList({!r})".format(self._items)

class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList({!r})".format(self._items)


if __name__ == "__main__":
    from pprint import pprint as pp

    sl = SortedList([4,3,78,11])
    print(sl)

    sl.add(-42)
    print(sl)

    sl.add(7)
    print(sl)

    il = IntList([1,2,3,4])
    il.add(19)
    # il.add('5')   # raises an exception TypeError

    sil = SortedIntList([42, 23, 2])
    sil.add(-23)
    print(sil)
    # sil = SortedIntList([3, 2, '1'])    # raises exception

    print(SortedIntList.__bases__)
    pp(SortedIntList.__mro__)    # tuple
    pp(SortedIntList.mro())      # list