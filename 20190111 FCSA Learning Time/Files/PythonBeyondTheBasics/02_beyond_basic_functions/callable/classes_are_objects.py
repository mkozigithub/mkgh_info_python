def sequence_class(immutable):
    return tuple if immutable else list

# def sequence_class(immutable):
#     if immutable:
#         cls = tuple
#     else:
#         cls = list
#     return cls

if __name__ == '__main__':
    seq = sequence_class(immutable= True)
    t = seq("Timbuktu")
    print(t)
    print(type(t))

    seq = sequence_class(immutable=False)
    l = seq("Timbuktu")
    print(l)
    print(type(l))
