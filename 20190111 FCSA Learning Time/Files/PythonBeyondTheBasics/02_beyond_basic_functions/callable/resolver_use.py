from resolver import Resolver

r = Resolver()

print(r.has_host('cnn.com'))

print(r('cnn.com'))
print(r('msn.com'))
print(r._cache)
print(r('cnn.com'))

r('amazon.com')
# short for:
r.__call__('amazon.com')

print(r.has_host('amazon.com'))
r.clear_cache()
print(r.has_host('amazon.com'))
