import pathlib
print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} starting")


def run_query():
    print("db run a query")


print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} ending")
