# @contextlib.contextmanager
# def my_context_manager():
#     # <ENTER>
#     try:
#         yeild [value]  # the value that is assigned to the as variable in the with statement
#         # <NORMAL EXIT>

#     except:
#         # <EXCEPTIONAL EXIT>  # exception raised in with block are redirected here
#         raise

# with my_context_manager() as x:
#     # ...

# Exceptions:
# * Use standard exception handling to propogate exceptions
# * Explicitly re-raise - or don't catch - to propogate exceptions
# * Swallow exceptions by not re-raising them


import contextlib
import sys

@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield 'You are in a with-block!'
        print('logging_context_manager: normal exit')
    except:
        print('logging_manager_context: exceptional exit!', sys.exc_info())
        raise # a bare raise statement will propogate the exception out of the context manager


def main():
    with logging_context_manager() as x:
        print(x)

    with logging_context_manager() as x:
        raise ValueError("error, error ...")


if __name__ == "__main__":
    main()

