import pathlib
print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} starting")


def do_something():
    print("socket do something.")


print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} ending")
