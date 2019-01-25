class ExampleIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        rslt = self.data[self.index]
        self.index += 1
        return rslt

class ExampleIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return ExampleIterator(self.data)

class AlternateInterable:
    def __init__(self):
        self.data = [1, 2, 3]

    def __getitem__(self, idx):
        return self.data[idx]


if __name__ == "__main__":
    i = ExampleIterator([1, 2, 3])
    print(next(i))
    print(next(i))
    print(next(i))
    # print(next(i)) # raises StopIteration exception

    for item in ExampleIterator(range(1, 4)):
        print(f"from for loop: {item}")

    for item in ExampleIterable(range(100, 104)):
        print(f"from another loop: {item}")

    x = [i**2 for i in ExampleIterable(range(5))]
    print(x)

    for item in AlternateInterable():
        print(f"using AlternateIterable: {item}")

    y = AlternateInterable();
    # print(y[4])  # raises IndexError exception

