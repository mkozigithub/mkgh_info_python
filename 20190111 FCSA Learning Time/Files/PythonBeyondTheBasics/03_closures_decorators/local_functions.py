from pprint import pprint as pp

def func():
    def local_func():
        a = 'hello'
        b = 'world'
        return a + b
    
    x = 1
    y = 2
    return x + y

store = []

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)  # each definition of last_letter results in a new last_letter function
    print(last_letter)
    return sorted(strings, key=last_letter)

g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    inner()

def enclosing():
    def local_func():
        print('local func')
    return local_func


if __name__ == "__main__":
    l = ['welcome', 'from', 'a', 'local', 'function']
    pp(sort_by_last_letter(l))
    pp(sort_by_last_letter(l))
    pp(sort_by_last_letter(l))

    outer()

    lf = enclosing()
    lf()