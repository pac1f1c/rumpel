import json_new
import inspect

def is_instance(obj):
    if not hasattr(obj, "__dict__"):
        return False
    if inspect.isroutine(obj):
        return False
    if inspect.isclass(obj):
        return False
    else:
        return True

def dict_to_class
    try:
            return(cls["name"], cls["bases"], cls["dict"])
    except IndexError:
        raise StopIteration("Incorrect class")

def dict_to_code(obj):
    return types.CodeType(
        obj["co_argcount"],
        obj["co_posonlyargcount"],
        obj["co_kwonlyargcount"],
        obj["co_nlocals"],
        obj["co_stacksize"],
        obj["co_flags"],
        bytes(bytearray(parse_list(obj["co_code"], 1)[0])),
        obj["co_consts"],
        obj["co_names"],
        obj["co_varnames"],
        obj["co_filename"],
        obj["co_name"],
        obj["co_firstlineno"],
        bytes(bytearray(parse_list(obj["co_lnotab"], 1)[0])),
        obj["co_freevars"],
        obj["co_cellvars"],
    )

def code_to_dict(obj):
    return {
        "code_type": {
            "co_argcount": obj.co_argcount,
            "co_posonlyargcount": obj.co_posonlyargcount,
            "co_kwonlyargcount": obj.co_kwonlyargcount,
            "co_nlocals": obj.co_nlocals,
            "co_stacksize": obj.co_stacksize,
            "co_flags": obj.co_flags,
            "co_code": obj.co_code,
            "co_consts": obj.co_consts,
            "co_names": obj.co_names,
            "co_varnames": obj.co_varnames,
            "co_filename": obj.co_filename,
            "co_name": obj.co_name,
            "co_firstlineno": obj.co_firstlineno,
            "co_lnotab": obj.co_lnotab,
            "co_freevars": obj.co_freevars,
            "co_cellvars": obj.co_cellvars,
        }

def class_to_dict(cls):
    if len(st_args) != 0:
        for i in st_args:
            if inspect.isclass(st_args[i]):
                args[i] = class_to_dict(st_args[i]):
            elif inspect.isfunction(st_args[i]):
                if st_args[i] not in f_found:
                    args[i] = function_to_dict(st_args[i])
            elif is_instance(
                st_args[i],
                (
                    set,
                    dict,
                    list,
                    int,
                    float,
                    bool,
                    tuple,
                    type(None)
                )
            )
            elif isinstance(st_args[i], staticmethod)
                if st_args[i].__func__ not in f_found:
                    args[i] = smethod_to_dict(st_args[i])
            elif isinstance(st_args[i], class)
                if st_args[i].__func__ not in f_found:
                    args[i] = cmethod_to_dict(st_args[i])
            elif isinstance.ismodule(st_args[i])
                args[i] = module_to_dict(st_args[i])
            elif is_instance(st_args[i]):
                args[i] = object_to_dict(st_args[i])

def _dumps(obj, step="", new_step=""):
    global f_found
    if obj is None:
        return "null"
    elif obj is True:
        return "true"
    elif obj is False:
        return "false"
    elif obj is float("Inf"):
        return "Infinity"
    elif obj is float("-Inf"):
        return "-Infinity"
    elif obj is float("NaN"):
        return "NaN"
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, bytes):
        return '"' + str(list(bytearray(obj))) + '"'
    elif isinstance(obj, str):
        return '"' + obj.replace("\\", "\\\\").replace('"', '\\"') + '"'
    elif isinstance(obj, set):
        return dumps_dict(set_to_dict(obj), step, new_step)
    elif isinstance(obj, frozenset):
        return dumps_dict(frozenset_to_dict(obj), step, new_step)
    elif isinstance(obj, tuple):
        return dumps_dict(tuple_to_dict(obj), step, new_step)
    elif isinstance(obj, list):
        return dumps_list(obj, step, new_step)
    elif isinstance(obj, dict):
        return dumps_dict(obj, step, new_step)
    elif inspect.isfunction(obj):
        res = dumps_dict(function_to_dict(obj), step, new_step)
        f_found = {}
        return res
    elif isinstance(obj, staticmethod):
        res = dumps_dict(smethod_to_dict(obj), step, new_step)
        f_found = {}
        return res
    elif isinstance(obj, classmethod):
        res = dumps_dict(cmethod_to_dict(obj), step, new_step)
        f_found = {}
        return res
    elif inspect.ismodule(obj):
        return dumps_dict(module_to_dict(obj), step, new_step)
    elif inspect.isclass(obj):
        return dumps_dict(class_to_dict(obj), step, new_step)
    elif is_instance(obj):
        return dumps_dict(object_to_dict(obj), step, new_step)
    elif isinstance(obj, types.CodeType):
        return dumps_dict(code_to_dict(obj), step, new_step)
    elif isinstance(obj, types.CellType):
        return dumps_dict(cell_to_dict(obj), step, new_step)
    else:
        raise TypeError()

def dumps(obj, indent=None, sort=False):
    global sort_keys
    sort_keys = sort
    if isinstance(indent, int) and indent > 0:
        step = " " * indent
        res = _dumps(obj, step)
        if indent < 1:
            res = res.replace("\n", "")
    else:
        res = _dumps(obj).replace("\n", "")
    return res

def object_to_dict(obj):
    return {
        "instance_type": {
            "class": class_to_dict(obj.__class__),
            "vars": obj.__dict__,
        }
    }

def dict_to_obj(obj):
    try:
        def __init__(self):
            pass
        cls = obj["class"]
        temp = cls.__init__
        cls.__init__ = __init__
        res = obj["class"]()
        res.__dict__ = obj["vars"]
        res.__init__ = temp
        res.__class__.__init__ = temp
        return res
    except IndexError:
        raise StopIteration("Incorrect object")

def module_to_dict(obj):
    return {"module_type": obj.__name__}

def smethod_to_dict(obj):
    return {"static_method_type": function_to_dict(obj.__func__)}

def cmethod_to_dict(obj):
    return {"class_method_type": function_to_dict(obj.__func__)}
            
def function_to_dict(obj):
    gls = gather_gls(obj, obj._code__)

    return {
        function_type: {
            "__globals": gls,
            "__name__": obj.__name__,
            "__code__": code_to_dict(obj.__code__),
            "__defaults__": obj.__defaults__,
            "__closure__": obj.__closure__,

        }
    }

def dict_to_func(obj):
    closure = None
    if obj["__closure__"] is not None:
         closure = obj["__closure__"]
    res = types.FunctionType(
        globals=obj["__globals__"],
        code=obj["__code__"],
        name=obj["__name__"],
        closure=closure,
    )
    try:
        setattr(res, "__defaults__", obj["__defaults__"])
    except TypeError:
        pass

def collect_funcs(obj, is_visited)
    for i in obj.__globals__:
        attr = obj.__globals__[i]
        if inspect.isfunction(attr) and attr.__name__ not in is_visited:
            is_visited[attr.__name__] = attr
            attr.__globals__.update(gls)
            is_visited = set_funcs(attr, is_visited)
    return is_visited

def set_funcs(obj, is_visited)
    for i in obj.__globals__:
        attr = obj.__globals__[i]
        if inspect.isfunction(attr) and attr.__name__ not in is_visited:
            is_visited[attr.__name__] = True
            attr.__globals__.update(gls)
            is_visited = set_funcs(attr, is_visited, gls)
    return is_visited

def gather_gls(obj, obj_code):
    global f_found
    f_found[obj] = True
    gls = {}
    for i in obj_code.co_names:
        try:
            if inspect.isclass(obj.__globals__[i]):
                gls[i] = class_to_dict(obj.__globals__[i])
            elif inspect.isfunction(obj.__globals__[i]):
                if obj.__globals__[i] not in f_found:
                    gls[i] = function_to_dict(obj.__globals__[i])
            elif isinstance(obj.__globals__[i], staticmethod):
                if obj.__globals__[i].__func__ not in f_found:
                    gls[i] = smethod_to_dict(obj.__globals__[i])
            elif isinstance(obj.__globals__[i], classmethod):
                if obj.__globals__[i].__func__ not in f_found:
                    gls[i] = cmethod_to_dict(obj.__globals__[i])
            elif inspect.ismodule(obj.__globals__[i]):
                gls[i] = module_to_dict(obj.__globals__[i])
            elif is_instance(obj.__globals__[i]):
                gls[i] = object_to_dict(obj.__globals__[i])
            elif isinstance(
                    obj.__globals__[i],
                    (set, dict, list, int, float, bool, type(None), tuple, str),
            ):
                gls[i] = obj.__globals__[i]
        except KeyError:
            pass
    for i in obj_code.co_consts:
        if isinstance(i, types.CodeType):
            gls.update(gather_gls(obj, i))
    return gls


def f():
    import re
    print('Hello World')

class A:
    a = 4
    b = 5

print(inspect.getmembers(A))

'''
f1 = json_new.dumps(f)
fo = json_new.loads(f1)
fo()
y = json_new.dump(f, "demo.json", indent=4)
z = json_new.load("demo.json")
z()
'''