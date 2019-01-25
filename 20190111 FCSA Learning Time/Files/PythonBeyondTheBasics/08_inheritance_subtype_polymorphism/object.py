'''
object is root of every method resolution order (MRO), is default base class when no base class defined.
object is the ultimate base class of every every class
'''
from simple_list import *
from pprint import pprint as pp

pp(list.mro())
pp(int.mro())
pp(SortedIntList.mro())

class NoBaseClass: pass
print(NoBaseClass.__bases__)
pp(dir(object))