def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [atr for atr in dir(obj) if not callable(getattr(obj, atr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    dict_int = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}
    return dict_int


number_info = introspection_info()
print(number_info)
