'''
Super():
Given a method resolution order (MRO) and a class C,
super() gives an object which resolves methods using
only the part of the mro which comes after C.
So, super() works on an MRO, and not directly on the base
classes of a class - works in the context of the MRO of the 
class it was called on.

Super() returns a proxy that routes method calls.  Bound proxies 
are bound to a class or a class instance.

super() uses everything  after a specific class in an MRO
to resolve method calls
'''

from pprint import pprint as pp
from simple_list import *

pp(SortedIntList.mro())
proxy = super(SortedList, SortedIntList)
pp(proxy)
pp(proxy.add)

proxy = super(SortedIntList, SortedIntList)
proxy._validate(5)
# proxy._validate("Whaaa?")  # raises error

# super(int, IntList) # raises exception if second arg is not a subclass of the first arg

sil = SortedIntList([5, 15, 10])
print(repr(sil))
proxy = super(SortedList, sil)
print(repr(proxy))
proxy.add(7)  # calls add on SimpleList
proxy.add('blah') # calls add on SimpleList
pp(repr(sil))

# super() with no arguments
'''
in an instance method super() ===> super(class-of-method, self)
In a class method super() ===> super(class-of-method, class)
'''
sil.add(5) 
'''
establishes MRO as MRO for SortedIntList, all calls to super() in base classes use the sil MRO, so
SortedIntList.add --> IntList.add (super() uses sil MRO) -->  SortedList.add (super() uses sil MRO) --->  SimpleList.add
'''
