# Python object serailizer

## Основной функционал предствлен в модуле json_new.py
Используются 4 основные команды:
- dumps(obj, indent) - преобразование объекта в строку json, возврат полученный строки
- dump(obj, fp, indent) - преобразование объекта в строку json, запись полученный строки в файл
- loads(string) - преобразование в объект из строки содержащей json описание
- load(fp) - преобразование объекта из файла, который содержит json описание

Сериализатор умеет работать с объектами типа:
- число
- строка
- список
- кортеж
- set
- frozenset
- функция (с closure включительно)
- класс
- объект класса
- статический метод
- метод класса
- объект типа code или cell

## ConsoleTool.py, которая позволяет преобразовывать объект в модуле в json формат с возможностью записи в файл и вывода на экран.
Представлены следующие флаги:
- --source : адрес файла из которого берется объекта (Принимается строка)
- --name : имя объекта в файле, который сериализуется (Принимается строка)
- --indent (-i) : количество пробелов для отступа (Принимается число)
- --sort (-s) : сортировка ключей в словарях (Принимается без аргумента)
- --file (-f) : адрес файла для сохранения сериализованного объекта (Принимается строка)
- --hide (-hh) : скрывает вывод сериализованного json текста (Принимается без аргумента)
-c --conf_file : утилита берет аргументы из файла конфигурации по указанному адресу (Принимается строка)

source и name - обязательные флаги

Пример использования:

python3 ConsoleTool.py --source json_new.py --name dumps

<details>
<summary>
Пример вывода:
</summary>
{
 "##function_type##": {
  "__globals__": {
   "sort_keys": false,
   "_dumps": {
    "##function_type##": {
     "__globals__": {
      "dumps_dict": {
       "##function_type##": {
        "__globals__": {
         "sort_keys": false
        },
        "__name__": "dumps_dict",
        "__code__": {
         "##code_type##": {
          "co_argcount": 3,
          "co_posonlyargcount": 0,
          "co_kwonlyargcount": 0,
          "co_nlocals": 6,
          "co_stacksize": 10,
          "co_flags": 67,
          "co_code": "[116, 0, 124, 0, 131, 1, 115, 12, 100, 1, 83, 0, 116, 1, 114, 32, 116, 2, 116, 3, 124, 0, 160, 4, 161, 0, 131, 1, 131, 1, 125, 0, 100, 2, 124, 2, 23, 0, 125, 2, 100, 3, 124, 2, 23, 0, 125, 3, 116, 5, 124, 0, 131, 1, 125, 4, 124, 4, 100, 0, 100, 4, 133, 2, 25, 0, 68, 0, 93, 68, 125, 5, 124, 3, 124, 1, 100, 5, 23, 0, 116, 6, 124, 5, 131, 1, 23, 0, 100, 5, 23, 0, 100, 6, 23, 0, 116, 7, 124, 0, 124, 5, 25, 0, 124, 1, 124, 2, 160, 8, 100, 2, 100, 7, 161, 2, 124, 1, 23, 0, 131, 3, 23, 0, 100, 8, 23, 0, 124, 2, 23, 0, 55, 0, 125, 3, 113, 68, 124, 3, 124, 1, 100, 5, 23, 0, 116, 6, 124, 4, 100, 4, 25, 0, 131, 1, 23, 0, 100, 5, 23, 0, 100, 6, 23, 0, 116, 7, 124, 0, 124, 4, 100, 4, 25, 0, 25, 0, 124, 1, 124, 2, 160, 8, 100, 2, 100, 7, 161, 2, 124, 1, 23, 0, 131, 3, 23, 0, 124, 2, 23, 0, 100, 9, 23, 0, 55, 0, 125, 3, 124, 3, 83, 0]",
          "co_consts": [
           null,
           "{}",
           "
",
           "{",
           -1,
           "\"",
           ": ",
           "",
           ",",
           "}"
          ],
          "co_names": [
           "len",
           "sort_keys",
           "dict",
           "sorted",
           "items",
           "list",
           "str",
           "_dumps",
           "replace"
          ],
          "co_varnames": [
           "obj",
           "step",
           "new_step",
           "res",
           "keys",
           "i"
          ],
          "co_filename": "json_new.py",
          "co_name": "dumps_dict",
          "co_firstlineno": 348,
          "co_lnotab": "[0, 1, 8, 1, 4, 1, 4, 1, 16, 1, 8, 1, 8, 1, 8, 1, 16, 1, 2, 1, 2, 1, 2, 255, 2, 2, 6, 254, 2, 3, 2, 253, 2, 4, 2, 252, 2, 5, 26, 251, 2, 6, 2, 250, 2, 7, 2, 249, 2, 255, 6, 10, 2, 1, 2, 1, 2, 255, 2, 2, 10, 254, 2, 3, 2, 253, 2, 4, 2, 252, 2, 5, 30, 251, 2, 6, 2, 250, 2, 7, 2, 249, 2, 255, 4, 10]",
          "co_freevars": [],
          "co_cellvars": []
         }
        },
        "__defaults__": [
         "",
         ""
        ]
       }
      },
      "set_to_dict": {
       "##function_type##": {
        "__globals__": {},
        "__name__": "set_to_dict",
        "__code__": {
         "##code_type##": {
          "co_argcount": 1,
          "co_posonlyargcount": 0,
          "co_kwonlyargcount": 0,
          "co_nlocals": 1,
          "co_stacksize": 3,
          "co_flags": 67,
          "co_code": "[100, 1, 116, 0, 124, 0, 131, 1, 105, 1, 83, 0]",
          "co_consts": [
           null,
           "##set_type##"
          ],
          "co_names": [
           "list"
          ],
          "co_varnames": [
           "obj"
          ],
          "co_filename": "json_new.py",
          "co_name": "set_to_dict",
          "co_firstlineno": 495,
          "co_lnotab": "[0, 1]",
          "co_freevars": [],
          "co_cellvars": []
         }
        },
        "__defaults__": null
       }
      },
      "frozenset_to_dict": {
       "##function_type##": {
        "__globals__": {},
        "__name__": "frozenset_to_dict",
        "__code__": {
         "##code_type##": {
          "co_argcount": 1,
          "co_posonlyargcount": 0,
          "co_kwonlyargcount": 0,
          "co_nlocals": 1,
          "co_stacksize": 3,
          "co_flags": 67,
          "co_code": "[100, 1, 116, 0, 124, 0, 131, 1, 105, 1, 83, 0]",
          "co_consts": [
           null,
           "##frozenset_type##"
          ],
          "co_names": [
           "list"
          ],
          "co_varnames": [
           "obj"
          ],
          "co_filename": "json_new.py",
          "co_name": "frozenset_to_dict",
          "co_firstlineno": 499,
          "co_lnotab": "[0, 1]",
          "co_freevars": [],
          "co_cellvars": []
         }
        },
        "__defaults__": null
       }
      },
      "tuple_to_dict": {
       "##function_type##": {
        "__globals__": {},
        "__name__": "tuple_to_dict",
        "__code__": {
         "##code_type##": {
          "co_argcount": 1,
          "co_posonlyargcount": 0,
          "co_kwonlyargcount": 0,
          "co_nlocals": 1,
          "co_stacksize": 3,
          "co_flags": 67,
          "co_code": "[100, 1, 116, 0, 124, 0, 131, 1, 105, 1, 83, 0]",
          "co_consts": [
           null,
           "##tuple_type##"
          ],
          "co_names": [
           "list"
          ],
          "co_varnames": [
           "obj"
          ],
          "co_filename": "json_new.py",
          "co_name": "tuple_to_dict",
          "co_firstlineno": 503,
          "co_lnotab": "[0, 1]",
          "co_freevars": [],
          "co_cellvars": []
         }
        },
        "__defaults__": null
       }
      },
      "dumps_list": {
       "##function_type##": {
        "__globals__": {},
        "__name__": "dumps_list",
        "__code__": {
         "##code_type##": {
          "co_argcount": 3,
          "co_posonlyargcount": 0,
          "co_kwonlyargcount": 0,
          "co_nlocals": 5,
          "co_stacksize": 10,
          "co_flags": 67,
          "co_code": "[116, 0, 124, 0, 131, 1, 115, 12, 100, 1, 83, 0, 100, 2, 124, 2, 23, 0, 125, 2, 100, 3, 124, 2, 23, 0, 125, 3, 116, 1, 116, 0, 124, 0, 131, 1, 100, 4, 24, 0, 131, 1, 68, 0, 93, 48, 125, 4, 124, 3, 124, 1, 116, 2, 124, 0, 124, 4, 25, 0, 124, 1, 124, 2, 160, 3, 100, 2, 100, 5, 161, 2, 124, 1, 23, 0, 131, 3, 23, 0, 100, 6, 23, 0, 124, 2, 23, 0, 55, 0, 125, 3, 113, 44, 124, 3, 124, 1, 116, 2, 124, 0, 100, 7, 25, 0, 124, 1, 124, 2, 160, 3, 100, 2, 100, 5, 161, 2, 124, 1, 23, 0, 131, 3, 23, 0, 124, 2, 23, 0, 100, 8, 23, 0, 55, 0, 125, 3, 124, 3, 83, 0]",
          "co_consts": [
           null,
           "[]",
           "
",
           "[",
           1,
           "",
           ",",
           -1,
           "]"
          ],
          "co_names": [
           "len",
           "range",
           "_dumps",
           "replace"
          ],
          "co_varnames": [
           "obj",
           "step",
           "new_step",
           "res",
           "i"
          ],
          "co_filename": "json_new.py",
          "co_name": "dumps_list",
          "co_firstlineno": 330,
          "co_lnotab": "[0, 1, 8, 1, 4, 1, 8, 1, 8, 1, 20, 1, 2, 1, 2, 1, 26, 255, 2, 2, 2, 254, 2, 3, 2, 253, 2, 255, 6, 6, 2, 1, 38, 255, 4, 3]",
          "co_freevars": [],
          "co_cellvars": []
         }
        },
        "__defaults__": [
         "",
         ""
        ]
       }
      },
      "inspect": {
       "##module_type##": "inspect"
      },
      "function_to_dict": {
       "##function_type##": {
        "__globals__": {
         "gather_gls": {
          "##function_type##": {
           "__globals__": {
            "f_found": {},
            "inspect": {
             "##module_type##": "inspect"
            },
            "class_to_dict": {
             "##function_type##": {
              "__globals__": {
               "__name__": "temp",
               "inspect": {
                "##module_type##": "inspect"
               },
               "f_found": {},
               "smethod_to_dict": {
                "##function_type##": {
                 "__globals__": {},
                 "__name__": "smethod_to_dict",
                 "__code__": {
                  "##code_type##": {
                   "co_argcount": 1,
                   "co_posonlyargcount": 0,
                   "co_kwonlyargcount": 0,
                   "co_nlocals": 1,
                   "co_stacksize": 3,
                   "co_flags": 67,
                   "co_code": "[100, 1, 116, 0, 124, 0, 106, 1, 131, 1, 105, 1, 83, 0]",
                   "co_consts": [
                    null,
                    "##static_method_type##"
                   ],
                   "co_names": [
                    "function_to_dict",
                    "__func__"
                   ],
                   "co_varnames": [
                    "obj"
                   ],
                   "co_filename": "json_new.py",
                   "co_name": "smethod_to_dict",
                   "co_firstlineno": 469,
                   "co_lnotab": "[0, 1]",
                   "co_freevars": [],
                   "co_cellvars": []
                  }
                 },
                 "__defaults__": null
                }
               },
               "cmethod_to_dict": {
                "##function_type##": {
                 "__globals__": {},
                 "__name__": "cmethod_to_dict",
                 "__code__": {
                  "##code_type##": {
                   "co_argcount": 1,
                   "co_posonlyargcount": 0,
                   "co_kwonlyargcount": 0,
                   "co_nlocals": 1,
                   "co_stacksize": 3,
                   "co_flags": 67,
                   "co_code": "[100, 1, 116, 0, 124, 0, 106, 1, 131, 1, 105, 1, 83, 0]",
                   "co_consts": [
                    null,
                    "##class_method_type##"
                   ],
                   "co_names": [
                    "function_to_dict",
                    "__func__"
                   ],
                   "co_varnames": [
                    "obj"
                   ],
                   "co_filename": "json_new.py",
                   "co_name": "cmethod_to_dict",
                   "co_firstlineno": 473,
                   "co_lnotab": "[0, 1]",
                   "co_freevars": [],
                   "co_cellvars": []
                  }
                 },
                 "__defaults__": null
                }
               },
               "module_to_dict": {
                "##function_type##": {
                 "__globals__": {
                  "__name__": "temp"
                 },
                 "__name__": "module_to_dict",
                 "__code__": {
                  "##code_type##": {
                   "co_argcount": 1,
                   "co_posonlyargcount": 0,
                   "co_kwonlyargcount": 0,
                   "co_nlocals": 1,
                   "co_stacksize": 2,
                   "co_flags": 67,
                   "co_code": "[100, 1, 124, 0, 106, 0, 105, 1, 83, 0]",
                   "co_consts": [
                    null,
                    "##module_type##"
                   ],
                   "co_names": [
                    "__name__"
                   ],
                   "co_varnames": [
                    "obj"
                   ],
                   "co_filename": "json_new.py",
                   "co_name": "module_to_dict",
                   "co_firstlineno": 431,
                   "co_lnotab": "[0, 1]",
                   "co_freevars": [],
                   "co_cellvars": []
                  }
                 },
                 "__defaults__": null
                }
               },
               "is_instance": {
                "##function_type##": {
                 "__globals__": {
                  "inspect": {
                   "##module_type##": "inspect"
                  }
                 },
                 "__name__": "is_instance",
                 "__code__": {
                  "##code_type##": {
                   "co_argcount": 1,
                   "co_posonlyargcount": 0,
                   "co_kwonlyargcount": 0,
                   "co_nlocals": 1,
                   "co_stacksize": 3,
                   "co_flags": 67,
                   "co_code": "[116, 0, 124, 0, 100, 1, 131, 2, 115, 14, 100, 2, 83, 0, 116, 1, 160, 2, 124, 0, 161, 1, 114, 28, 100, 2, 83, 0, 116, 1, 160, 3, 124, 0, 161, 1, 114, 42, 100, 2, 83, 0, 100, 3, 83, 0, 100, 0, 83, 0]",
                   "co_consts": [
                    null,
                    "__dict__",
                    false,
                    true
                   ],
                   "co_names": [
                    "hasattr",
                    "inspect",
                    "isroutine",
                    "isclass"
                   ],
                   "co_varnames": [
                    "obj"
                   ],
                   "co_filename": "json_new.py",
                   "co_name": "is_instance",
                   "co_firstlineno": 8,
                   "co_lnotab": "[0, 1, 10, 1, 4, 1, 10, 1, 4, 1, 10, 1, 4, 2]",
                   "co_freevars": [],
                   "co_cellvars": []
                  }
                 },
                 "__defaults__": null
                }
               },
               "object_to_dict": {
                "##function_type##": {
                 "__globals__": {},
                 "__name__": "object_to_dict",
                 "__code__": {
                  "##code_type##": {
                   "co_argcount": 1,
                   "co_posonlyargcount": 0,
                   "co_kwonlyargcount": 0,
                   "co_nlocals": 1,
                   "co_stacksize": 4,
                   "co_flags": 67,
                   "co_code": "[100, 1, 116, 0, 124, 0, 106, 1, 131, 1, 124, 0, 106, 2, 100, 2, 156, 2, 105, 1, 83, 0]",
                   "co_consts": [
                    null,
                    "##instance_type##",
                    [
                     "class",
                     "vars"
                    ]
                   ],
                   "co_names": [
                    "class_to_dict",
                    "__class__",
                    "__dict__"
                   ],
                   "co_varnames": [
                    "obj"
                   ],
                   "co_filename": "json_new.py",
                   "co_name": "object_to_dict",
                   "co_firstlineno": 422,
                   "co_lnotab": "[0, 2, 2, 1, 8, 1, 4, 254, 4, 255]",
                   "co_freevars": [],
                   "co_cellvars": []
                  }
                 },
                 "__defaults__": null
                }
               }
              },
              "__name__": "class_to_dict",
              "__code__": {
               "##code_type##": {
                "co_argcount": 1,
                "co_posonlyargcount": 0,
                "co_kwonlyargcount": 0,
                "co_nlocals": 5,
                "co_stacksize": 11,
                "co_flags": 67,
                "co_code": "[100, 1, 125, 1, 116, 0, 124, 0, 106, 1, 131, 1, 100, 2, 107, 3, 114, 54, 124, 0, 106, 1, 68, 0, 93, 28, 125, 2, 124, 2, 106, 2, 100, 3, 107, 3, 114, 24, 124, 1, 116, 3, 124, 2, 131, 1, 102, 1, 55, 0, 125, 1, 113, 24, 105, 0, 125, 3, 116, 4, 124, 0, 106, 5, 131, 1, 125, 4, 116, 0, 124, 4, 131, 1, 100, 2, 107, 3, 144, 1, 114, 122, 124, 4, 68, 0, 144, 1, 93, 32, 125, 2, 116, 6, 160, 7, 124, 4, 124, 2, 25, 0, 161, 1, 114, 124, 116, 3, 124, 4, 124, 2, 25, 0, 131, 1, 124, 3, 124, 2, 60, 0, 113, 86, 116, 6, 160, 8, 124, 4, 124, 2, 25, 0, 161, 1, 114, 168, 124, 4, 124, 2, 25, 0, 116, 9, 118, 1, 114, 166, 116, 10, 124, 4, 124, 2, 25, 0, 131, 1, 124, 3, 124, 2, 60, 0, 113, 86, 116, 11, 124, 4, 124, 2, 25, 0, 116, 12, 131, 2, 114, 214, 124, 4, 124, 2, 25, 0, 106, 13, 116, 9, 118, 1, 114, 212, 116, 14, 124, 4, 124, 2, 25, 0, 131, 1, 124, 3, 124, 2, 60, 0, 113, 86, 116, 11, 124, 4, 124, 2, 25, 0, 116, 15, 131, 2, 144, 1, 114, 8, 124, 4, 124, 2, 25, 0, 106, 13, 116, 9, 118, 1, 144, 1, 114, 120, 116, 16, 124, 4, 124, 2, 25, 0, 131, 1, 124, 3, 124, 2, 60, 0, 113, 86, 116, 6, 160, 17, 124, 4, 124, 2, 25, 0, 161, 1, 144, 1, 114, 42, 116, 18, 124, 4, 124, 2, 25, 0, 131, 1, 124, 3, 124, 2, 60, 0, 113, 86, 116, 19, 124, 4, 124, 2, 25, 0, 131, 1, 144, 1, 114, 74, 116, 20, 124, 4, 124, 2, 25, 0, 131, 1, 124, 3, 124, 2, 60, 0, 113, 86, 116, 11, 124, 4, 124, 2, 25, 0, 116, 21, 116, 4, 116, 22, 116, 23, 116, 24, 116, 25, 116, 26, 100, 0, 131, 1, 116, 27, 102, 8, 131, 2, 114, 86, 124, 4, 124, 2, 25, 0, 124, 3, 124, 2, 60, 0, 113, 86, 100, 4, 124, 0, 106, 2, 124, 1, 124, 3, 100, 5, 156, 3, 105, 1, 83, 0]",
                "co_consts": [
                 null,
                 [],
                 0,
                 "object",
                 "##class_type##",
                 [
                  "name",
                  "bases",
                  "dict"
                 ]
                ],
                "co_names": [
                 "len",
                 "__bases__",
                 "__name__",
                 "class_to_dict",
                 "dict",
                 "__dict__",
                 "inspect",
                 "isclass",
                 "isfunction",
                 "f_found",
                 "function_to_dict",
                 "isinstance",
                 "staticmethod",
                 "__func__",
                 "smethod_to_dict",
                 "classmethod",
                 "cmethod_to_dict",
                 "ismodule",
                 "module_to_dict",
                 "is_instance",
                 "object_to_dict",
                 "set",
                 "list",
                 "int",
                 "float",
                 "bool",
                 "type",
                 "tuple"
                ],
                "co_varnames": [
                 "cls",
                 "dpns",
                 "i",
                 "args",
                 "st_args"
                ],
                "co_filename": "json_new.py",
                "co_name": "class_to_dict",
                "co_firstlineno": 380,
                "co_lnotab": "[0, 1, 4, 1, 14, 1, 10, 1, 10, 1, 16, 1, 4, 1, 10, 1, 14, 1, 10, 1, 14, 1, 18, 1, 14, 1, 12, 1, 18, 1, 14, 1, 14, 1, 18, 1, 16, 1, 16, 1, 18, 1, 16, 1, 18, 1, 14, 1, 18, 1, 2, 1, 6, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 6, 1, 2, 248, 2, 254, 4, 13, 14, 1]",
                "co_freevars": [],
                "co_cellvars": []
               }
              },
              "__defaults__": null
             }
            },
            "types": {
             "##module_type##": "types"
            }
           },
           "__name__": "gather_gls",
           "__code__": {
            "##code_type##": {
             "co_argcount": 2,
             "co_posonlyargcount": 0,
             "co_kwonlyargcount": 0,
             "co_nlocals": 4,
             "co_stacksize": 12,
             "co_flags": 67,
             "co_code": "[100, 1, 116, 0, 124, 0, 60, 0, 105, 0, 125, 2, 124, 1, 106, 1, 68, 0, 144, 1, 93, 96, 125, 3, 144, 1, 122, 68, 116, 2, 160, 3, 124, 0, 106, 4, 124, 3, 25, 0, 161, 1, 114, 66, 116, 5, 124, 0, 106, 4, 124, 3, 25, 0, 131, 1, 124, 2, 124, 3, 60, 0, 144, 1, 110, 26, 116, 2, 160, 6, 124, 0, 106, 4, 124, 3, 25, 0, 161, 1, 114, 116, 124, 0, 106, 4, 124, 3, 25, 0, 116, 0, 118, 1, 114, 114, 116, 7, 124, 0, 106, 4, 124, 3, 25, 0, 131, 1, 124, 2, 124, 3, 60, 0, 110, 232, 116, 8, 124, 0, 106, 4, 124, 3, 25, 0, 116, 9, 131, 2, 114, 168, 124, 0, 106, 4, 124, 3, 25, 0, 106, 10, 116, 0, 118, 1, 114, 166, 116, 11, 124, 0, 106, 4, 124, 3, 25, 0, 131, 1, 124, 2, 124, 3, 60, 0, 110, 180, 116, 8, 124, 0, 106, 4, 124, 3, 25, 0, 116, 12, 131, 2, 114, 220, 124, 0, 106, 4, 124, 3, 25, 0, 106, 10, 116, 0, 118, 1, 114, 218, 116, 13, 124, 0, 106, 4, 124, 3, 25, 0, 131, 1, 124, 2, 124, 3, 60, 0, 110, 128, 116, 2, 160, 14, 124, 0, 106, 4, 124, 3, 25, 0, 161, 1, 144, 1, 114, 2, 116, 15, 124, 0, 106, 4, 124, 3, 25, 0, 131, 1, 124, 2, 124, 3, 60, 0, 110, 90, 116, 16, 124, 0, 106, 4, 124, 3, 25, 0, 131, 1, 144, 1, 114, 38, 116, 17, 124, 0, 106, 4, 124, 3, 25, 0, 131, 1, 124, 2, 124, 3, 60, 0, 110, 54, 116, 8, 124, 0, 106, 4, 124, 3, 25, 0, 116, 18, 116, 19, 116, 20, 116, 21, 116, 22, 116, 23, 116, 24, 100, 0, 131, 1, 116, 25, 116, 26, 102, 9, 131, 2, 144, 1, 114, 92, 124, 0, 106, 4, 124, 3, 25, 0, 124, 2, 124, 3, 60, 0, 87, 0, 113, 18, 4, 0, 116, 27, 144, 1, 121, 114, 1, 0, 1, 0, 1, 0, 89, 0, 113, 18, 48, 0, 113, 18, 124, 1, 106, 28, 68, 0, 93, 36, 125, 3, 116, 8, 124, 3, 116, 29, 106, 30, 131, 2, 144, 1, 114, 124, 124, 2, 160, 31, 116, 32, 124, 0, 124, 3, 131, 2, 161, 1, 1, 0, 144, 1, 113, 124, 124, 2, 83, 0]",
             "co_consts": [
              null,
              true
             ],
             "co_names": [
              "f_found",
              "co_names",
              "inspect",
              "isclass",
              "__globals__",
              "class_to_dict",
              "isfunction",
              "function_to_dict",
              "isinstance",
              "staticmethod",
              "__func__",
              "smethod_to_dict",
              "classmethod",
              "cmethod_to_dict",
              "ismodule",
              "module_to_dict",
              "is_instance",
              "object_to_dict",
              "set",
              "dict",
              "list",
              "int",
              "float",
              "bool",
              "type",
              "tuple",
              "str",
              "KeyError",
              "co_consts",
              "types",
              "CodeType",
              "update",
              "gather_gls"
             ],
             "co_varnames": [
              "obj",
              "obj_code",
              "gls",
              "i"
             ],
             "co_filename": "json_new.py",
             "co_name": "gather_gls",
             "co_firstlineno": 435,
             "co_lnotab": "[0, 2, 8, 1, 4, 1, 12, 1, 4, 1, 16, 1, 22, 1, 16, 1, 14, 1, 20, 1, 16, 1, 16, 1, 20, 1, 16, 1, 16, 1, 20, 1, 18, 1, 20, 1, 16, 1, 20, 1, 2, 1, 8, 1, 24, 254, 6, 4, 18, 1, 14, 1, 8, 1, 10, 1, 14, 1, 20, 1]",
             "co_freevars": [],
             "co_cellvars": []
            }
           },
           "__defaults__": null
          }
         },
         "__name__": "temp",
         "code_to_dict": {
          "##function_type##": {
           "__globals__": {},
           "__name__": "code_to_dict",
           "__code__": {
            "##code_type##": {
             "co_argcount": 1,
             "co_posonlyargcount": 0,
             "co_kwonlyargcount": 0,
             "co_nlocals": 1,
             "co_stacksize": 18,
             "co_flags": 67,
             "co_code": "[100, 1, 124, 0, 106, 0, 124, 0, 106, 1, 124, 0, 106, 2, 124, 0, 106, 3, 124, 0, 106, 4, 124, 0, 106, 5, 124, 0, 106, 6, 124, 0, 106, 7, 124, 0, 106, 8, 124, 0, 106, 9, 124, 0, 106, 10, 124, 0, 106, 11, 124, 0, 106, 12, 124, 0, 106, 13, 124, 0, 106, 14, 124, 0, 106, 15, 100, 2, 156, 16, 105, 1, 83, 0]",
             "co_consts": [
              null,
              "##code_type##",
              [
               "co_argcount",
               "co_posonlyargcount",
               "co_kwonlyargcount",
               "co_nlocals",
               "co_stacksize",
               "co_flags",
               "co_code",
               "co_consts",
               "co_names",
               "co_varnames",
               "co_filename",
               "co_name",
               "co_firstlineno",
               "co_lnotab",
               "co_freevars",
               "co_cellvars"
              ]
             ],
             "co_names": [
              "co_argcount",
              "co_posonlyargcount",
              "co_kwonlyargcount",
              "co_nlocals",
              "co_stacksize",
              "co_flags",
              "co_code",
              "co_consts",
              "co_names",
              "co_varnames",
              "co_filename",
              "co_name",
              "co_firstlineno",
              "co_lnotab",
              "co_freevars",
              "co_cellvars"
             ],
             "co_varnames": [
              "obj"
             ],
             "co_filename": "json_new.py",
             "co_name": "code_to_dict",
             "co_firstlineno": 507,
             "co_lnotab": "[0, 2, 2, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 240, 4, 255]",
             "co_freevars": [],
             "co_cellvars": []
            }
           },
           "__defaults__": null
          }
         }
        },
        "__name__": "function_to_dict",
        "__code__": {
         "##code_type##": {
          "co_argcount": 1,
          "co_posonlyargcount": 0,
          "co_kwonlyargcount": 0,
          "co_nlocals": 2,
          "co_stacksize": 7,
          "co_flags": 67,
          "co_code": "[116, 0, 124, 0, 124, 0, 106, 1, 131, 2, 125, 1, 100, 1, 124, 1, 124, 0, 106, 2, 116, 3, 124, 0, 106, 1, 131, 1, 124, 0, 106, 4, 124, 0, 106, 5, 100, 2, 156, 5, 105, 1, 83, 0]",
          "co_consts": [
           null,
           "##function_type##",
           [
            "__globals__",
            "__name__",
            "__code__",
            "__defaults__",
            "__closure__"
           ]
          ],
          "co_names": [
           "gather_gls",
           "__code__",
           "__name__",
           "code_to_dict",
           "__defaults__",
           "__closure__"
          ],
          "co_varnames": [
           "obj",
           "gls"
          ],
          "co_filename": "json_new.py",
          "co_name": "function_to_dict",
          "co_firstlineno": 477,
          "co_lnotab": "[0, 1, 12, 3, 2, 1, 2, 1, 4, 1, 8, 1, 4, 1, 4, 251, 4, 255]",
          "co_freevars": [],
          "co_cellvars": []
         }
        },
        "__defaults__": null
       }
      },
      "f_found": {},
      "types": {
       "##module_type##": "types"
      },
      "cell_to_dict": {
       "##function_type##": {
        "__globals__": {},
        "__name__": "cell_to_dict",
        "__code__": {
         "##code_type##": {
          "co_argcount": 1,
          "co_posonlyargcount": 0,
          "co_kwonlyargcount": 0,
          "co_nlocals": 1,
          "co_stacksize": 2,
          "co_flags": 67,
          "co_code": "[100, 1, 124, 0, 106, 0, 105, 1, 83, 0]",
          "co_consts": [
           null,
           "##cell_type##"
          ],
          "co_names": [
           "cell_contents"
          ],
          "co_varnames": [
           "obj"
          ],
          "co_filename": "json_new.py",
          "co_name": "cell_to_dict",
          "co_firstlineno": 491,
          "co_lnotab": "[0, 1]",
          "co_freevars": [],
          "co_cellvars": []
         }
        },
        "__defaults__": null
       }
      }
     },
     "__name__": "_dumps",
     "__code__": {
      "##code_type##": {
       "co_argcount": 3,
       "co_posonlyargcount": 0,
       "co_kwonlyargcount": 0,
       "co_nlocals": 4,
       "co_stacksize": 5,
       "co_flags": 67,
       "co_code": "[124, 0, 100, 0, 117, 0, 114, 12, 100, 1, 83, 0, 124, 0, 100, 2, 117, 0, 114, 24, 100, 3, 83, 0, 124, 0, 100, 4, 117, 0, 114, 36, 100, 5, 83, 0, 124, 0, 116, 0, 100, 6, 131, 1, 117, 0, 114, 52, 100, 7, 83, 0, 124, 0, 116, 0, 100, 8, 131, 1, 117, 0, 114, 68, 100, 9, 83, 0, 124, 0, 116, 0, 100, 10, 131, 1, 117, 0, 114, 84, 100, 10, 83, 0, 116, 1, 124, 0, 116, 2, 116, 0, 102, 2, 131, 2, 114, 106, 116, 3, 124, 0, 131, 1, 83, 0, 116, 1, 124, 0, 116, 4, 131, 2, 114, 140, 100, 11, 116, 3, 116, 5, 116, 6, 124, 0, 131, 1, 131, 1, 131, 1, 23, 0, 100, 11, 23, 0, 83, 0, 116, 1, 124, 0, 116, 3, 131, 2, 114, 178, 100, 11, 124, 0, 160, 7, 100, 12, 100, 13, 161, 2, 160, 7, 100, 11, 100, 14, 161, 2, 23, 0, 100, 11, 23, 0, 83, 0, 116, 1, 124, 0, 116, 8, 131, 2, 114, 204, 116, 9, 116, 10, 124, 0, 131, 1, 124, 1, 124, 2, 131, 3, 83, 0, 116, 1, 124, 0, 116, 11, 131, 2, 144, 0, 114, 232, 116, 9, 116, 12, 124, 0, 131, 1, 124, 1, 124, 2, 131, 3, 83, 0, 116, 1, 124, 0, 116, 13, 131, 2, 144, 1, 114, 4, 116, 9, 116, 14, 124, 0, 131, 1, 124, 1, 124, 2, 131, 3, 83, 0, 116, 1, 124, 0, 116, 5, 131, 2, 144, 1, 114, 28, 116, 15, 124, 0, 124, 1, 124, 2, 131, 3, 83, 0, 116, 1, 124, 0, 116, 16, 131, 2, 144, 1, 114, 52, 116, 9, 124, 0, 124, 1, 124, 2, 131, 3, 83, 0, 116, 17, 160, 18, 124, 0, 161, 1, 144, 1, 114, 88, 116, 9, 116, 19, 124, 0, 131, 1, 124, 1, 124, 2, 131, 3, 125, 3, 105, 0, 97, 20, 124, 3, 83, 0, 116, 1, 124, 0, 116, 21, 131, 2, 144, 1, 114, 124, 116, 9, 116, 22, 124, 0, 131, 1, 124, 1, 124, 2, 131, 3, 125, 3, 105, 0, 97, 20, 124, 3, 83, 0, 116, 1, 124, 0, 116, 23, 131, 2, 144, 1, 114, 160, 116, 9, 116, 24, 124, 0, 131, 1, 124, 1, 124, 2, 131, 3, 125, 3, 105, 0, 97, 20, 124, 3, 83, 0, 116, 17, 160, 25, 124, 0, 161, 1, 144, 1, 114, 188, 116, 9, 116, 26, 124, 0, 131, 1, 124, 1, 124, 2, 131, 3, 83, 0, 116, 17, 160, 27, 124, 0, 161, 1, 144, 1, 114, 216, 116, 9, 116, 28, 124, 0, 131, 1, 124, 1, 124, 2, 131, 3, 83, 0, 116, 29, 124, 0, 131, 1, 144, 1, 114, 242, 116, 9, 116, 30, 124, 0, 131, 1, 124, 1, 124, 2, 131, 3, 83, 0, 116, 1, 124, 0, 116, 31, 106, 32, 131, 2, 144, 2, 114, 16, 116, 9, 116, 33, 124, 0, 131, 1, 124, 1, 124, 2, 131, 3, 83, 0, 116, 1, 124, 0, 116, 31, 106, 34, 131, 2, 144, 2, 114, 46, 116, 9, 116, 35, 124, 0, 131, 1, 124, 1, 124, 2, 131, 3, 83, 0, 116, 36, 131, 0, 130, 1, 100, 0, 83, 0]",
       "co_consts": [
        null,
        "null",
        true,
        "true",
        false,
        "false",
        "Inf",
        "Infinity",
        "-Inf",
        "-Infinity",
        "NaN",
        "\"",
        "\\",
        "\\\\",
        "\\\""
       ],
       "co_names": [
        "float",
        "isinstance",
        "int",
        "str",
        "bytes",
        "list",
        "bytearray",
        "replace",
        "set",
        "dumps_dict",
        "set_to_dict",
        "frozenset",
        "frozenset_to_dict",
        "tuple",
        "tuple_to_dict",
        "dumps_list",
        "dict",
        "inspect",
        "isfunction",
        "function_to_dict",
        "f_found",
        "staticmethod",
        "smethod_to_dict",
        "classmethod",
        "cmethod_to_dict",
        "ismodule",
        "module_to_dict",
        "isclass",
        "class_to_dict",
        "is_instance",
        "object_to_dict",
        "types",
        "CodeType",
        "code_to_dict",
        "CellType",
        "cell_to_dict",
        "TypeError"
       ],
       "co_varnames": [
        "obj",
        "step",
        "new_step",
        "res"
       ],
       "co_filename": "json_new.py",
       "co_name": "_dumps",
       "co_firstlineno": 530,
       "co_lnotab": "[0, 2, 8, 1, 4, 1, 8, 1, 4, 1, 8, 1, 4, 1, 12, 1, 4, 1, 12, 1, 4, 1, 12, 1, 4, 1, 14, 1, 8, 1, 10, 1, 24, 1, 10, 1, 28, 1, 10, 1, 16, 1, 12, 1, 16, 1, 12, 1, 16, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 16, 1, 4, 1, 4, 1, 12, 1, 16, 1, 4, 1, 4, 1, 12, 1, 16, 1, 4, 1, 4, 1, 12, 1, 16, 1, 12, 1, 16, 1, 10, 1, 16, 1, 14, 1, 16, 1, 14, 1, 16, 2]",
       "co_freevars": [],
       "co_cellvars": []
      }
     },
     "__defaults__": [
      "",
      ""
     ]
    }
   }
  },
  "__name__": "dumps",
  "__code__": {
   "##code_type##": {
    "co_argcount": 3,
    "co_posonlyargcount": 0,
    "co_kwonlyargcount": 0,
    "co_nlocals": 5,
    "co_stacksize": 4,
    "co_flags": 67,
    "co_code": "[124, 2, 97, 0, 116, 1, 124, 1, 116, 2, 131, 2, 114, 62, 124, 1, 100, 1, 107, 4, 114, 62, 100, 2, 124, 1, 20, 0, 125, 3, 116, 3, 124, 0, 124, 3, 131, 2, 125, 4, 124, 1, 100, 3, 107, 0, 114, 78, 124, 4, 160, 4, 100, 4, 100, 5, 161, 2, 125, 4, 110, 16, 116, 3, 124, 0, 131, 1, 160, 4, 100, 4, 100, 5, 161, 2, 125, 4, 124, 4, 83, 0]",
    "co_consts": [
     null,
     0,
     " ",
     1,
     "
",
     ""
    ],
    "co_names": [
     "sort_keys",
     "isinstance",
     "int",
     "_dumps",
     "replace"
    ],
    "co_varnames": [
     "obj",
     "indent",
     "sort",
     "step",
     "res"
    ],
    "co_filename": "json_new.py",
    "co_name": "dumps",
    "co_firstlineno": 586,
    "co_lnotab": "[0, 2, 4, 1, 18, 1, 8, 1, 10, 1, 8, 1, 14, 2, 16, 1]",
    "co_freevars": [],
    "co_cellvars": []
   }
  },
  "__defaults__": [
   null,
   false
  ]
 }
}
</details>
<function dumps at 0x0000028252E59CA0>
