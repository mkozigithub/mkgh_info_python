def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


def color(red, green, blue, **kwargs):
    print(f"red = {red}")
    print(f"green = {green}")
    print(f"blue = {blue}")
    print(kwargs)


def run():
    t = (11, 12, 13, 14)
    print_args(*t)

    k = {'red': 21, 'green': 68, 'blue':120, 'alpha': 52}
    color(**k)

    k2 = dict(red=21, green=68, blue=120, alpha=52)  # inititialzer uses **kwargs technique to create a dictionary 
    color(**k2)

if __name__ == "__main__":
    run()
