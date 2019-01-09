class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'

    def __format__(self, f):
        if f == 'r':
            return f'[{self.y}, {self.x}]'
        else:
            return f'[{self.x}, {self.y}]'



class Defaults:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p1 = Point2D(4, 6)
    print(str(p1))
    print(repr(p1))

    print(Point2D(5,6))

    print(Defaults(4,5))  # print calls str(), which defaults to calling repr()

    l = [Point2D(i, i*2) for i in range(3)]
    print(str(l))   # repr used for sub elements
    print(repr(l))  # repr used for sub elements

    d = {i: Point2D(i, i*2) for i in range(3)}
    print(str(d))   # repr used for sub elements
    print(repr(d))  # repr used for sub elements

    print(f"This is a point {Defaults(101,102)}")  # this calls __format__, which defaults to __str__ if not defined
    print(f"This is a point {Point2D(101,102)}")  # this calls __format__, which defaults to __str__ if not defined
    print(f"This is a point {Point2D(101,102):r}")  # :f - f is passed into __format__
    print("This is a point {!s}".format(Point2D(101,102)))  # !s force use of __str__
    print("This is a point {!r}".format(Point2D(101,102)))  # !r force use of __repr__

    import reprlib  # drop in replacement for repr() (handles large strings better)
    points = [Point2D(x, y) for x in range(1000) for y in range(1000)]
    print(len(points))
    print(reprlib.repr(points))   # truncates the string to a managable length
    ##  more details about reprlib at: https://docs.python.org/3/library/reprlib.html

    # ascii() changes non ascii chars into an escape sequence
    non_ascii = "\u00C7 \u00D8"
    print(non_ascii, ascii(non_ascii))

    c = "\u046C"
    o = ord(c)
    print(c)
    print(o)
    print(chr(o))
    print(ord(c))