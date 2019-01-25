from random import randrange

def main():
    number = randrange(100)
    while True:
        try:
            guess = int(input("? "))
        # except:  # try to always catch specific errors, catching all errors can lead to problems
        except ValueError:
            continue
        if guess == number:
            print("You win!")
            break


if __name__ == "__main__":
    main()