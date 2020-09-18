import pathlib
print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} starting")


def function_at_root_module_level():
    print("socket root-level function")


print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} ending")
