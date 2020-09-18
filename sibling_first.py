import sibling_second
from sibling_second import same_name_func


try:
    calls_something_in_second()
except NameError:
    print("The call to calls_something_in_second() failed because the function hasn't been defined yet.")


def same_name_func():
    print("This comes from sibling_first.py")


def calls_something_in_second():
    print("calling 'same_name_func()'")
    same_name_func()
    print("calling 'sibling_second.same_name_func()'")
    sibling_second.same_name_func()


calls_something_in_second()
print("[not-in-a-function] sibling_first.py loaded.")
