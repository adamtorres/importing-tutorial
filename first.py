def hello(arg):
    print(f"Hello.  You passed in {arg}.")


def generic_func():
    print("generic_func() from first")


print("This print is not inside of a function.")


def dict_func_example_a(x):
    print(f"dict_func_example_a({x})")


def dict_func_example_b(x):
    print(f"dict_func_example_b({x})")


def dict_func_example_c(x):
    print(f"dict_func_example_c({x})")


def dict_func_example_default(x):
    print(f"no function matches. {x}")


def dict_func_example(arg):
    pick_one = {
        'a': dict_func_example_a,
        'b': dict_func_example_b,
        'c': dict_func_example_c,
    }
    func = pick_one.get(arg[0], dict_func_example_default)
    func(arg)


def not_using_dict_func_example(arg):
    first_char = arg[0]
    if first_char == 'a':
        dict_func_example_a(arg)
    elif first_char == 'b':
        dict_func_example_b(arg)
    elif first_char == 'c':
        dict_func_example_c(arg)
    else:
        dict_func_example_default(arg)
