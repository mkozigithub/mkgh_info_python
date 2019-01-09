from resolver import Resolver

type(Resolver)
type(Resolver.__call__)

# Resolver() is the 'callable' for the class object Resolver: it invokes Resolver.__call__, which ultimately produces an instance of Resolver
#  so Resolver() is a factory function for producing resolver.Resolver objects (instance object of type resolver.Resolver)
resolve = Resolver()
type(resolve)

print(Resolver)
print(resolve)

print(vars()['Resolver'])
print(vars()['resolve'])

