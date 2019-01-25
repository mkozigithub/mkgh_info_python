# arbitrary number of args, positional arguments
# print()
# print("one")
# print("one", "two", "three")

# x = "{a}<====>{b}".format(a="Oslo", b="Stavanger")
# print(x)

# *args handles additional positional arguments
# **kwargs handles keyword arguments

def hypervolume_base(*args):
    print(args)
    print(type(args))

def hypervolume_1(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v

def hypervolume_2(length, *lengths):
    v = length
    for length in lengths:
        v *= length
    return v


def tag_base(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))

def tag_1(name, **attributes):
    result = f'<{name}'
    for key, value in attributes.items():
        result += f' {key}:"{value}"'
    return f"{result}>"

def tag_2(name, **attributes):
    attributes = "".join([f' {key}:"{value}"' for key, value in attributes.items()])
    return f"<{name} {attributes}>"

# invalid syntax_1: ** must come after *
# def syntax(**kwargs, *args):
#     pass

# any arguments after the *args must be passed in by name or results in TypeError
def syntax_2(arg1, arg2, *args, kwarg1, kwarg2):
    print(arg1)
    print(arg2)
    print(*args)
    print(kwarg1)
    print(kwarg2)

# extended **kwargs must come last
def syntax_3(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(*args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)


if __name__ == "__main__":
    hypervolume_base()
    hypervolume_base(3,4)

    print(hypervolume_1(2,4))
    print(hypervolume_1(2, 4, 6))
    print(hypervolume_1(2, 4, 6, 8))
    # print(hypervolume_1())  # throws StopIteration exception


    print(hypervolume_2(2,4))
    # print(hypervolume_2())  # throws normal TypeError exception, due to missing required positional argument

    tag_base('img', src="monet.jpg", alt="Sunrise by Claude Monet", border=1)
    print(tag_1('img', src="monet.jpg", alt="Sunrise by Claude Monet", border=1))
    print(tag_2('img', src="monet.jpg", alt="Sunrise by Claude Monet", border=1))

    # syntax_1()

    # any parameters passed after the *args must be passed as named args
    # syntax_2(1, 2, 3, 4, 5, 6, 7) # throws a TypeError: missing 2 required keyword-only arguments 'kwarg1', 'kwarg2'
    syntax_2(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7)

    # additional extended keyword args must be last
    syntax_3(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7, kwargs3=8, kwargs4=9)