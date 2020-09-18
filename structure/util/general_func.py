import pathlib
print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} starting")


def commonly_useful_function():
    print("util commonly_useful_function")


print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} ending")
