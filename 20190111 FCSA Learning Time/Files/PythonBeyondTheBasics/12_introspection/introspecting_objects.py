from pprint import pprint as pp

i = 7
pp(dir(i))
print(2, getattr(i, 'numerator'), getattr(i, 'denominator'), i.denominator)
print(getattr(i, 'conjugate'), callable(getattr(i, 'conjugate')), i.conjugate.__class__.__name__)
print(hasattr(i, 'bit_length'), hasattr(i, 'index'))

# introspection for scopes
pp(globals())
a = 42
pp(globals())
globals()['tau'] = 6.283185
pp(globals())
print(tau / 2)

def report_scope(arg):
    from pprint import pprint as pp1
    x = 496
    pp1(locals(), width=10)

report_scope(42)


import inspect
import sorted_set

print(f"ismodule: {inspect.ismodule(sorted_set)}")
# pp(inspect.getmembers(sorted_set))  # returns everything in module
pp(inspect.getmembers(sorted_set, inspect.isclass))

from sorted_set import chain
l = list(chain([1, 2, 3], [4, 5, 6]))
print(l)

pp(inspect.getmembers(sorted_set.SortedSet, inspect.isfunction))

init_sig = inspect.signature(sorted_set.SortedSet.__init__)
print(init_sig, init_sig.parameters)
print(init_sig.parameters['items'].default)