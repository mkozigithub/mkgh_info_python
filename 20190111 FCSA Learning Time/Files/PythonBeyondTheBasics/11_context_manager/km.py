class TestContextManager:
    def __enter__(self):
        print("TestContextManager.__enter__()")
        return "You are in a with block!!"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("TextContextManager.__exit__(): normal exit detected")
        else:
            print(f"TestContextManager.__exit__(): exception detected type={exc_type}, value={exc_val}, traceback={exc_tb}")
        return


def main():
    with TestContextManager() as x:
        print(x)
    
    # with TestContextManager() as x:
    #     raise ValueError("Somethings wrong!")  # __exit__() still called

    try:
        with TestContextManager() as x:
            raise ValueError('The system is down!')  # error in body is propogated out of the __exit__() method
    except ValueError:
        print('*** ValueError detected ***')


if __name__ == "__main__":
    main()