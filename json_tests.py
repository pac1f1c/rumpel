import unittest
import test3
import json_new


def converter(obj):
    return json_new.loads(json_new.dumps(obj))


class TestSerializer(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)

    def test_empty_object(self):
        objects = test3.objects
        self.assertEqual(objects, converter(objects))

    def test_simple_string(self):
        objects = test3.string
        self.assertEqual(objects, converter(objects))

    def test_simple_obj_1(self):
        objects = test3.t1
        self.assertEqual(objects, converter(objects))

    def test_simple_obj_2(self):
        objects = test3.t2
        self.assertEqual(objects, converter(objects))

    def test_simple_obj_3(self):
        objects = test3.t3
        self.assertEqual(objects, converter(objects))

    def test_simple_func(self):
        objects = test3.simple_func
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(), converter(objects)())

    def test_recursion_func(self):
        objects = test3.simple_recursion
        self.assertEqual(objects.__code__, converter(objects.__code__))
        try:
            converter(objects)()
        except RecursionError:
            pass

    def test_cycle_recursion_func(self):
        objects = test3.double_func_recursion_2
        self.assertEqual(objects.__code__, converter(objects.__code__))
        try:
            converter(objects)()
        except RecursionError:
            pass

    def test_func_with_globals_and_builtins(self):
        objects = test3.func_with_globals_and_builtins
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(), converter(objects)())

    def test_func_in_func(self):
        objects = test3.func_in_func
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(2, 3, 4), converter(objects)(2, 3, 4))

    def test_func_with_defaults(self):
        objects = test3.func_with_defaults
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(), converter(objects)())

    def test_tuple_returner(self):
        objects = test3.tuple_returner
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(2, 3, 4, 5), converter(objects)(2, 3, 4, 5))

    def test_set_returner(self):
        objects = test3.set_returner
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(2, 3, 4, 5), converter(objects)(2, 3, 4, 5))

    def test_func_with_args_sum(self):
        objects = test3.func_with_args_sum
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(2, 3, 4, 5), converter(objects)(2, 3, 4, 5))

    def test_func_with_args_d(self):
        objects = test3.func_with_args_d
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(a=4,b=3), converter(objects)(a=4,b=3))

    def test_decorator(self):

        def test_func():
            return 'hh'

        objects = test3.counter
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(test_func)(), converter(objects)(test_func)())

    def test_check_decorator(self):
        objects = test3.check_decorator
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(), converter(objects)())

    def test_simplified_defaults(self):
        objects = test3.p
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects()(), converter(objects)()())

    def test_simple_lambda(self):
        objects = test3.simplelambda
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(3), converter(objects)(3))

    def test_lambda_in_lambda(self):
        objects = test3.lambda_in_lambda
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(3), converter(objects)(3))

    def test_lambda_in_function(self):
        objects = test3.lambda_in_function
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(3), converter(objects)(3))

    def test_some_decorators(self):
        objects = test3.some_decorators
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(3), converter(objects)(3))

    def test_Empty_cls(self):
        objects = test3.Empty_cls
        converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(converter(objects)(), i))

    def test_Cls_with_inheritance(self):
        objects = test3.Simple_cls
        converter(objects)(5,6)
        for i in objects(5,6).__dict__:
            self.assertEqual(getattr(objects(2,3), i), getattr(converter(objects)(2,3), i))

    def test_Cls_with_inheritance(self):
        objects = test3.Cls_with_inheritance
        converter(objects)(5,6)
        for i in objects(5,6).__dict__:
            self.assertEqual(getattr(objects(2,3), i), getattr(converter(objects)(2,3), i))

    def test_Cls_with_staticmethod(self):
        objects = test3.Cls_with_staticmethod
        converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(converter(objects)(), i))

    def test_Cls_with_classmethod(self):
        objects = test3.Cls_with_classmethod
        converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(converter(objects)(), i))

    def test_Inherited_cls(self):
        objects = test3.Inherited_cls
        converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(converter(objects)(), i))

    def test_Cls_with_class_and_static_methods(self):
        objects = test3.B
        converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(converter(objects)(), i))