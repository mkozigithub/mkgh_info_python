
if __name__ == "__main__":
    # extended iter(): can be used to produce infinite iterables
    import datetime
    import time

    i = iter(datetime.datetime.now, None)
    print(next(i))
    time.sleep(.1)
    print(next(i))
    time.sleep(.1)
    print(next(i))
    time.sleep(.1)
    print(next(i))


    import os
    print(__file__)
    print(os.path.dirname(__file__))

    with open(f'{os.path.dirname(__file__)}/ending_file.txt', 'rt') as f:
        for line in iter(lambda: f.readline().strip(), 'END'):
            print(line)