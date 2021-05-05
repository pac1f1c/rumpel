import inspect
import types

f_found = {}


def is_instance(obj):
    if not hasattr(obj, "__dict__"):
        return False
    if inspect.isroutine(obj):
        return False
    if inspect.isclass(obj):
        return False
    else:
        return True


def dict_to_module(obj):
    try:
        return __import__(obj)
    except ModuleNotFoundError:
        raise ImportError(str(obj) + " not found")


def dict_to_class(cls):
    try:
        return type(cls["name"], tuple(cls["bases"]), parse(cls["dict"]))
    except IndexError:
        raise StopIteration("Incorrect class")


def dict_to_obj(obj):
    try:

        def __init__(self):
            pass

        cls = parse(obj["class"])
        temp = cls.__init__
        cls.__init__ = __init__
        res = obj["class"]()
        res.__dict__ = obj["vars"]
        res.__init__ = temp
        res.__class__.__init__ = temp
        return res
    except IndexError:
        raise StopIteration("Incorrect object")


def dict_to_code(obj):
    return types.CodeType(
        obj["co_argcount"],
        obj["co_posonlyargcount"],
        obj["co_kwonlyargcount"],
        obj["co_nlocals"],
        obj["co_stacksize"],
        obj["co_flags"],
        obj["co_code"],
        obj["co_consts"],
        obj["co_names"],
        obj["co_varnames"],
        obj["co_filename"],
        obj["co_name"],
        obj["co_firstlineno"],
        obj["co_lnotab"],
        obj["co_freevars"],
        obj["co_cellvars"],
    )


def collect_funcs(obj, is_visited):
    for i in obj.__globals__:
        attr = obj.__globals__[i]
        if inspect.isfunction(attr) and attr.__name__ not in is_visited:
            is_visited[attr.__name__] = attr
            is_visited = collect_funcs(attr, is_visited)
    return is_visited


def set_funcs(obj, is_visited, gls):
    for i in obj.__globals__:
        attr = obj.__globals__[i]
        if inspect.isfunction(attr) and attr.__name__ not in is_visited:
            is_visited[attr.__name__] = True
            attr.__globals__.update(gls)
            is_visited = set_funcs(attr, is_visited, gls)
    return is_visited


def dict_to_func(obj):
    res = types.FunctionType(
        globals=parse(obj["__globals__"]),
        code=parse(obj["__code__"]),
        name=obj["__name__"],
    )

    try:
        setattr(res, "__defaults__", tuple(obj["__defaults__"]))
    except TypeError:
        pass
    funcs = collect_funcs(res, {})
    funcs.update({res.__name__: res})
    set_funcs(res, {res.__name__: True}, funcs)
    res.__globals__.update(funcs)
    res.__globals__["__builtins__"] = __import__("builtins")
    return res


def class_to_dict(cls):
    dpns = ()
    if len(cls.__bases__) != 0:
        for i in cls.__bases__:
            if i.__name__ != "object":
                dpns += (class_to_dict(i),)
    args = {}
    st_args = dict(cls.__dict__)
    if len(st_args) != 0:
        for i in st_args:
            if inspect.isclass(st_args[i]):
                args[i] = class_to_dict(st_args[i])
            elif inspect.isfunction(st_args[i]):
                if st_args[i].__name__ not in f_found:
                    args[i] = function_to_dict(st_args[i])
            elif isinstance(st_args[i], staticmethod):
                if st_args[i].__func__.__name__ not in f_found:
                    args[i] = staticmethod_to_dict(st_args[i])
            elif isinstance(st_args[i], classmethod):
                if st_args[i].__func__.__name__ not in f_found:
                    args[i] = classmethod_to_dict(st_args[i])
            elif inspect.ismodule(st_args[i]):
                args[i] = module_to_dict(st_args[i])
            elif is_instance(st_args[i]):
                args[i] = object_to_dict(st_args[i])
            elif isinstance(
                st_args[i],
                (set, frozenset, dict, list, int, float, bool, type(None), tuple),
            ):
                args[i] = st_args[i]
    return {"##class_type##": {"name": cls.__name__, "bases": dpns, "dict": args}}


def object_to_dict(obj):
    return {
        "##instance_type##": {
            "class": class_to_dict(obj.__class__),
            "vars": convert(obj.__dict__),
        }
    }


def module_to_dict(obj):
    return {"##module_type##": obj.__name__}


def gather_gls(obj, obj_code):
    f_found[obj.__name__] = True
    gls = {}
    for i in obj_code.co_names:
        try:
            if inspect.isclass(obj.__globals__[i]):
                gls[i] = class_to_dict(obj.__globals__[i])
            elif inspect.isfunction(obj.__globals__[i]):
                if obj.__globals__[i].__name__ not in f_found:
                    gls[i] = function_to_dict(obj.__globals__[i])
            elif isinstance(obj.__globals__[i], staticmethod):
                if obj.__globals__[i].__func__.__name__ not in f_found:
                    gls[i] = staticmethod_to_dict(obj.__globals__[i])
            elif isinstance(obj.__globals__[i], classmethod):
                if obj.__globals__[i].__func__.__name__ not in f_found:
                    gls[i] = classmethod_to_dict(obj.__globals__[i])
            elif inspect.ismodule(obj.__globals__[i]):
                gls[i] = module_to_dict(obj.__globals__[i])
            elif is_instance(obj.__globals__[i]):
                gls[i] = object_to_dict(obj.__globals__[i])
            elif isinstance(
                obj.__globals__[i],
                (set, frozenset, dict, list, int, float, bool, type(None), tuple, str),
            ):
                gls[i] = obj.__globals__[i]
        except KeyError:
            pass
    for i in obj_code.co_consts:
        if isinstance(i, types.CodeType):
            gls.update(gather_gls(obj, i))
    return gls


def staticmethod_to_dict(obj):
    return {"##static_method_type##": function_to_dict(obj.__func__)}


def classmethod_to_dict(obj):
    return {"##class_method_type##": function_to_dict(obj.__func__)}


def function_to_dict(obj):
    gls = gather_gls(obj, obj.__code__)

    return {
        "##function_type##": {
            "__globals__": gls,
            "__name__": obj.__name__,
            "__code__": code_to_dict(obj.__code__),
            "__defaults__": obj.__defaults__,
        }
    }


def code_to_dict(obj):
    return {
        "##code_type##": {
            "co_argcount": obj.co_argcount,
            "co_posonlyargcount": obj.co_posonlyargcount,
            "co_kwonlyargcount": obj.co_kwonlyargcount,
            "co_nlocals": obj.co_nlocals,
            "co_stacksize": obj.co_stacksize,
            "co_flags": obj.co_flags,
            "co_code": obj.co_code,
            "co_consts": convert(obj.co_consts),
            "co_names": obj.co_names,
            "co_varnames": obj.co_varnames,
            "co_filename": obj.co_filename,
            "co_name": obj.co_name,
            "co_firstlineno": obj.co_firstlineno,
            "co_lnotab": obj.co_lnotab,
            "co_freevars": obj.co_freevars,
            "co_cellvars": obj.co_cellvars,
        }
    }


def convert(obj):
    if isinstance(obj, (str, int, float, bool, frozenset)) or obj is None:
        return obj
    elif isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = convert(obj[i])
        return obj
    elif isinstance(obj, set):
        obj = list(obj)
        for i in range(len(obj)):
            obj[i] = convert(obj[i])
        return set(obj)
    elif isinstance(obj, tuple):
        obj = list(obj)
        # for i in range(len(obj)):
        #    obj[i] = convert(obj[i])
        return tuple(obj)
    elif isinstance(obj, dict):
        res = {}
        for i in obj:
            res[i] = convert(obj[i])
        return res
    elif inspect.isfunction(obj):
        res = function_to_dict(obj)
        return res
    elif isinstance(obj, staticmethod):
        res = staticmethod_to_dict(obj)
        return res
    elif isinstance(obj, classmethod):
        res = classmethod_to_dict(obj)
        return res
    elif inspect.ismodule(obj):
        return module_to_dict(obj)
    elif inspect.isclass(obj):
        return class_to_dict(obj)
    elif is_instance(obj):
        return object_to_dict(obj)
    elif isinstance(obj, types.CodeType):
        return code_to_dict(obj)
    else:
        print(type(obj))
        raise TypeError(obj)


def parse(obj):
    if (
        isinstance(obj, (str, int, float, bool, bytes, set, frozenset, tuple))
        or obj is None
    ):
        return obj
    if isinstance(obj, list):
        res = []
        for i in obj:
            res.append(parse(i))
        return res
    elif isinstance(obj, dict):
        if "##function_type##" in obj and len(obj.keys()) == 1:
            return dict_to_func(obj["##function_type##"])
        if "##class_type##" in obj and len(obj.keys()) == 1:
            return dict_to_class(obj["##class_type##"])
        if "##static_method_type##" in obj and len(obj.keys()) == 1:
            return staticmethod(
                dict_to_func(obj["##static_method_type##"]["##function_type##"])
            )
        if "##class_method_type##" in obj and len(obj.keys()) == 1:
            return classmethod(
                dict_to_func(obj["##class_method_type##"]["##function_type##"])
            )
        if "##instance_type##" in obj and len(obj.keys()) == 1:
            return dict_to_obj(obj["##instance_type##"])
        if "##module_type##" in obj and len(obj.keys()) == 1:
            return dict_to_module(obj["##module_type##"])
        if "##code_type##" in obj and len(obj.keys()) == 1:
            return dict_to_code(obj["##code_type##"])
        res = {}
        for i in obj:
            res[i] = parse(obj[i])
        return res
    else:
        print(obj)
        raise TypeError()


def dumps(obj, indent=None):
    f_found = {}
    try:
        return __import__("pickle").dumps(convert(obj))
    except (TypeError, AttributeError) as e:
        raise EOFError(convert(obj))


def loads(obj):
    cur = __import__("pickle").loads(obj)
    return parse(cur)


def dump(obj, fp):
    try:
        with open(fp, "w") as file:
            file.write(dumps(obj))
    except FileNotFoundError:
        raise FileNotFoundError("file doesn't exist")


def load(fp):
    try:
        with open(fp, "r") as file:
            data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError("file doesn't exist")
    return loads(data)
