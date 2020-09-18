import pathlib
print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} starting")

from .structure_file_1 import open
from .structure_file_2 import move_file


def function_at_root_module_level():
    print("file root-level function")


print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} ending")
