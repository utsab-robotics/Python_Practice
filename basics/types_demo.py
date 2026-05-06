import builtins
import types
import inspect

print("===== BUILT-IN FUNCTIONS =====")
for name in dir(builtins):
    obj = getattr(builtins, name)
    if isinstance(obj, types.BuiltinFunctionType):
        print(name)

print("\n===== BUILT-IN CLASSES =====")
for name in dir(builtins):
    obj = getattr(builtins, name)
    if isinstance(obj, type):
        print(name)

print("\n===== METHODS OF LIST CLASS =====")
for name, obj in inspect.getmembers(list):
    if inspect.isfunction(obj) or inspect.ismethoddescriptor(obj):
        print(name)

print("\n===== METHODS OF STRING CLASS =====")
for name, obj in inspect.getmembers(str):
    if inspect.isfunction(obj) or inspect.ismethoddescriptor(obj):
        print(name)

print("\n===== METHODS OF DICT CLASS =====")
for name, obj in inspect.getmembers(dict):
    if inspect.isfunction(obj) or inspect.ismethoddescriptor(obj):
        print(name)