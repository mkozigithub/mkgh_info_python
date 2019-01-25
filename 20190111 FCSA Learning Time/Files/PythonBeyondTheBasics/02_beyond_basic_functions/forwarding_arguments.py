def trace(f, *args, **kwargs):
    print("args = ", args)
    print("kwargs = ", kwargs)
    result = f(*args, **kwargs)
    print("result = ", result)
    return result


trace(int, "ff", base=16)
trace(int, "34", base=8)