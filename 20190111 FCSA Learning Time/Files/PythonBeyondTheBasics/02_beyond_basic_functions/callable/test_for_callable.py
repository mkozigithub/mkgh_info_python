from resolver import Resolver

r = Resolver()
print(f"Resolver is callable: {callable(Resolver)}")
print(f"r is callable: {callable(r)}")
print(f"47 is callable: {callable(47)}")
print(f"'abcd' is callable: {callable('abcd')}")

def is_even():
    return x % 2 == 0
print(f"is_even is callable: {callable(is_even)}")

is_odd = lambda n: x % 2 != 0
print(f"is_odd is callable: {callable(is_odd)}")
