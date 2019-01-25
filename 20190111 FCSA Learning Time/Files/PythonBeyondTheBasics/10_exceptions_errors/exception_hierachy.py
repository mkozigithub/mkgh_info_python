# exception hierachy: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

def lookups():
    s = [1, 4, 6]
    try:
        item = s[5]
    except IndexError:
        print("Handled IndexError")

    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    except KeyError:
        print("Handled KeyError")   

    try:
        item = s[5]
    except LookupError:  # IndexError is subclass of LookupError, so is handled by except LookupError
        print("Handled LookupError")

    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    except LookupError:  # KeyError is subclass of LookupError, so is handled by except LookupError
        print("Handled LookupError")   


if __name__ == "__main__":
    s = [1, 4, 6]
    # s[5]  # IndexError
    print(IndexError.mro())

    d = dict(a=65, b=66, c=67)
    # d['x'] # KeyError
    print(KeyError.mro())

    lookups()