import pathlib
print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} starting")


def function_at_root_module_level():
    print("util root-level function")
    from . import general_func
    general_func.commonly_useful_function()


print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} ending")
