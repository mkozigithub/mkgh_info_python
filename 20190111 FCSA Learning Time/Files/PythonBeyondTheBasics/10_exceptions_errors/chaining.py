import math
import traceback

class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError("slope cannot be vertical") from e


def main():
    print(inclination(3, 5))

    try:
        print(inclination(0, 5))
    except InclinationError as e:
        print(e)
        print(e.__cause__)
        print(e.__traceback__)   
        traceback.print_tb(e.__traceback__)
        s = traceback.format_tb(e.__traceback__)
        print(s)  

    # print(inclination(0, 5))


if __name__ == "__main__":
    main()
    print("Finished")