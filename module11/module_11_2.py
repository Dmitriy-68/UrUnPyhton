import inspect


def introspection_info(obj):
    info_ = {}
    info_['тип'] = str(type(obj)).split("'")[1]
    info_['атрибуты'] = [attr for attr in dir(obj)
                         if not callable(getattr(obj, attr))
                         ]
    info_['методы'] = [method for method in dir(obj)
                       if callable(getattr(obj, method))
                       ]
    if inspect.getmodule(obj) is None:
        info_['модуль'] = 'None'
    else:
        info_['модуль'] = str(inspect.getmodule(obj)).split("'")[1]

    return info_


number_info = introspection_info(introspection_info)
print(number_info)

number_info = introspection_info(42)
print(number_info)
