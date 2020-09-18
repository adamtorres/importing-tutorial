import pathlib
print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} starting")


def open():
    print("socket open")


print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} ending")
