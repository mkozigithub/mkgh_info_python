_registry = []

def register(name):
    _registry.append(name)

def registered_names():
    return iter(_registry)