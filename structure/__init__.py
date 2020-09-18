"""
This is a doc string at the top of the doc.  It will be included if someone runs `help(structure)`.
"""

import pathlib
print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} starting")
from .io import db, file
from .io.socket import structure_socket_1, structure_socket_2

from . import util


def function_at_root_module_level():
    print("structure root-level function")


def do_some_db_stuff():
    db.function_at_root_module_level()
    db.open()
    db.run_query()


def do_some_file_stuff():
    file.function_at_root_module_level()
    file.open()
    file.move_file()


def do_some_socket_stuff():
    print("the socket.function_at_root_module_level is not accessible because of how the imports are written.")
    structure_socket_1.open()
    structure_socket_2.do_something()


def run_all():
    print("run_all() starting")
    do_some_db_stuff()
    do_some_file_stuff()
    do_some_socket_stuff()
    print("first call that has an import")
    util.function_at_root_module_level()
    print("second call that has an import")
    util.function_at_root_module_level()
    print("run_all() ending")


print(f"{__file__.replace(str(pathlib.Path('.').resolve()), '')} ending")
