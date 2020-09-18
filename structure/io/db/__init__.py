import pathlib
print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} starting")


from .structure_db_1 import open
from .structure_db_2 import run_query


def function_at_root_module_level():
    print("db root-level function")


print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} ending")
