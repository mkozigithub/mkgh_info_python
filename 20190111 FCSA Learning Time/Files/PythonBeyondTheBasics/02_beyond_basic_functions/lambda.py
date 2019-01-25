scientists = ['Marie Curie', 'Alber Einstein', 'Niels Borh', 'Isaac Newton', 'Dmitri Mendeleev', 'Antoine Lavoisier', 'Carl Linnaeus', 'Alfred Wegner', 'Chalres Darwin']
print(scientists)

s = sorted(scientists, key=lambda name: name.split()[-1])
print(s)

# lambda expression - body can contain only a single expression
last_name = lambda name: name.split()[-1]
print(type(last_name))
print(last_name(scientists[1]))

# equivalent to def statement:
def last_name_2(name):
    return name.split()[-1]