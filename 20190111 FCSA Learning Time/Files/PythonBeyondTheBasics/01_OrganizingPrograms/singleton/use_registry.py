import registry

registry.register("my name")
registry.register("other name")
for name in registry.registered_names():
    print(name)