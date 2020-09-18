import pathlib
print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} starting")


def move_file():
    print("file move file function")


print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} ending")
