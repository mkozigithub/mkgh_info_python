# https://www.python.org/dev/peps/pep-0343/
#   conceptually, a context manager:
#       with context-manager:
#           context-manager.begin()  # setup
#           body
#           context-manager.end()  # teardown - .end() runs even in the event of an exception in body()
# A context manager ensures that resources are properly and automatically managed

# context manager protocol:
#   __enter__(self)
#   __exit__(self, exc_type, exc_val, exc_tb)

# if the __exit__() returns False (or doesn't return anything), any exception raised in the body will be propogated out of the with statement
# if the __exit__() return True, exceptions raised in the body will be swallowed
# __exit__() should never re-raise exceptions


def main():
    with open('important_data.txt', 'w') as f:
        f.write('The secret password is 12345')

    f = open('a_file', 'w')
    with f as g:
        print(f"f is g: {f is g}")


if __name__ == "__main__":
    main()