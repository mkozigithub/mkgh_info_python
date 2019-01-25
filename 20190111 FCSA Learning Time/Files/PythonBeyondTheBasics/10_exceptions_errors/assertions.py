

def modulus_three(n):
    r = n % 3
    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Remainder 1")
    else:
        assert r == 2, "Remainder is not 2"
        print("Remainder 2")

def modulus_four(n):
    r = n % 4
    if r == 0:
        print("Multiple of 4")
    elif r == 1:
        print("Remainder 1")
    else:
        assert r == 2, "Remainder is not 2"
        print("Remainder 2")

def modulus_four_corrected(n):
    r = n % 4
    if r == 0:
        print("Multiple of 4")
    elif r == 1:
        print("Remainder 1")
    elif r == 2:
        print("Remainder 2")
    elif r == 3:
        print("Remainder 3")
    else:
        assert False, "This should never happen"


def main():
    assert 5 > 2, "This shouldn't fail"
    # assert False, "The condition was false"  # raises an AssertionError if condition is false

    print(modulus_three(5))
    # print(modulus_four(7))  # violates assertion and raises AssertionError
    print(modulus_four_corrected(7))


if __name__ == "__main__":
    main()
