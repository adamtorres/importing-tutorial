# Importing For Fun and Profit

Most applications are made up of many files.  This helps not only with organization but with reusability.  At the most basic level, it allows you to copy a source file that has some useful functions to another project.  In the more sustainable method, desired files can be gathered into a certain structure, packaged up, and submitted to PyPi.org.  That allows others to `pip install super-fancy-neat-package` and not have to worry about if they have the latest version.  They could add `--upgrade` to the command line and it would get the most recent version and replace any existing version.  That site is not the only source available for pip.  If you are in a company which does not want code to be public (or you simply don't want it to be), you can also `pip install git+https://github.com/github-username/super-fancy-neat-package`.
The point is, having all code in one monolithic source file is not the best route.  "Divide and conquer" and all that jazz.

----

## Table of Contents

 * [Initial Setup From Scratch](#initial-setup-from-scratch)
 * [Starting up](#starting-up)
 * [Getting Help From Python](#getting-help-from-python)
 * [Namespaces](#namespaces)
 * [Importing builtins](#importing-builtins)
 * [Importing your file](#importing-your-file)
   * [The dict Object](#the-dict-object)
   * [Square Brackets](#square-brackets)
   * [String Formatting](#string-formatting)
 * [Importing sibling file from your file](#importing-sibling-file-from-your-file)
 * [Circular imports](#circular-imports)
 * [Adding directory structures](#adding-directory-structures)
 * [Running a module](#running-a-module)
 * [Building your own runnable module](#building-your-own-runnable-module)

----

# Terminology

I tend to use "module" and "package" interchangeably and for possibly a variety of things.  The loose definition I use is "a grouping of functions/classes/variables/objects".  This can be a single file or a folder structure that has lots of files.  In general, I'll use "module" more often for the individual file and large set of folders while reserving "package" for a large set of folders.

Just now looked up the proper definition for [pacakge](https://docs.python.org/3/glossary.html#term-package) and [module](https://docs.python.org/3/glossary.html#term-module).  Seems a module is as I defined it above while a package is "\[t]echnically, a package is a Python module with an \_\_path__ attribute."

The phrase, "Google is your friend", comes to mind.  While they filter a variety of political/medical/etc things, I've not found much to show they filter coding pages.  Unless, of course, those pages also have political/medical/etc content.  Use DuckDuckGo, Bing, whatever.  To focus searches, add in "python" and possibly the framework being used.  As in, if you are trying to figure out how to change the default primary key field on a Django model, the search might look like "python django model custom primary key field".  It might take a few changes to the terms.  You'll get it after seeing what works.  Just know that most search engines are for natural language.  Certain symbols have specific meaning there.  Enclosing a few words in quotes will usually tell the engine you want results which have that phrase in its entirety.

A term not covered in the documentation linked earlier is "style guide".  Think of it as a guide for how the code should look.  It could cover everything from single/double quote usage, naming schemes, tabs/spaces, indentation, and other bits.  The goal of a guide is so someone has to expend less effort to understand the code if they are used to the defined style.  Having to decipher ever-changing indentation patters gets old real quick.  Another term that will come up with "style guide" is "PEP8".  "PEP" stands for "Python Enhancement Proposal".  These are documents for suggestions of improvements.  Similar to RFC (Request For Comment) but python-specific.  PEP8 is an almost 20 year old document spelling out details of style.  Quite a few tools (including PyCharm) base their style off of that document.

----

# Initial Setup From Scratch

Create the project folder and change into it.

```
mkdir importing
cd importing
```

Clone the repo into the current folder.  Note the ` .` at the end of the command.  Without it, a new folder will be created using the name of the repo.  With, it will use the stated folder (the current one in this case) as the root of the repo.  The destination folder needs to be empty for git to clone successfully.

```
git clone https://github.com/adamtorres/importing-tutorial .
```

Pretty much the only reason to do the cloning as above (with a ` .`) is so the folder on your local system is named what you want rather than whatever is the repo name.  Were you to run the clone without the ` .`, a new folder named "importing-tutorial" would be created and the contents placed there.  It was done here as an example.

Creating or cloning the repo will not create a functional virtual environment to run the examples.  The following commands use `pyenv` to create a virtual environment and then set the new virtual environment to be the active one for the current folder.

```
pyenv virtualenv --copies 3.8.5 importing_env
pyenv local importing_env
```

This assumes a few things.  You have `pyenv` and `pyenv-virtualenv` installed, and Python 3.8.5 is installed via `pyenv install 3.8.5`.

----

# Starting Up

Next, start the interactive interpreter.

```
python
```

It should show output similar to the following.

```
Python 3.8.5 (default, Aug 20 2020, 18:56:07)
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is the prompt waiting for commands.  You can do most things here that you can do in a script.  It is just a bit more difficult as if you were creating a long function and made a typo in a previous line, you cannot just scroll up and fix it.  Example, say you are creating a 4 line function and you make a typo on the 3rd line but don't catch it until you pressed enter to start the 4th line.  You'd have to redo all of the lines and remember to fix the typo when you get to the 3rd line.  On the plus side, pressing up arrow generally recalls previous lines.  While I wouldn't want to write a full application using this interface, it is handy for quick debugging/testing of isolated functions.  Copy/paste also works well - having a text doc with a variety of statements/functions to copy and paste into the terminal.

Of course, if something is repeated often enough, it would probably be better to just make a script for it.  Even if it is in a tmp folder and not committed to the repo.

----

# Getting Help From Python

Python includes some helper functions that are most useful on the interactive prompt.  It even reminds you of one of the functions on the 3rd line in the output when starting the interactive prompt.  The `help` function will show the help for the specified function or start an interactive help dialog when nothing is specified.

As an example, show some help on the `print` function.
```
>>> help(print)
```

The output starts as:
```
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

From the help shown above (the actual output details the arguments), it can be seen that the print function takes some number of positional arguments and a few named arguments.  Since this tutorial is not on the print function, that's as deep as we're going there.

For a class, the output is a little different.  This example calls help on itself.

```
>>> help(help)
```

The output starts as:

```
Help on _Helper in module _sitebuiltins object:

class _Helper(builtins.object)
 |  Define the builtin 'help'.
 |
 |  This is a wrapper around pydoc.help that provides a helpful message
 |  when 'help' is typed at the Python interactive prompt.
```

From that, we can see that `help` is actually a class and not just a function.  What makes it so we can treat it as a function is the `__call__` function seen in the following.

```
 |  __call__(self, *args, **kwds)
 |      Call self as a function.
```

For now, just note the difference in how the help is displayed between a function and a class.  Wandered a bit from the topic of this document.

That's all well and good if you know what you want help on.  Calling `help()` without any arguments will start the interactive help prompt where you can browse some of the internals.

```
>>> help()
```

The important bit in the initial output is this line: 

```
To get a list of available modules, keywords, symbols, or 
topics, type "modules", "keywords", "symbols", or "topics".
```

Also note the prompt has changed from `>>>` to `help>`.  To exit the help prompt, just press enter on an empty line.

From here, you can type `modules`, `keywords`, etc and see a listing of such to get further help on just by typing the terms.

As a shortcut, you can include the terms in the initial `help()` call.  For example, to see the listing of modules without having to start the interactive bit, add `'modules'` to the call.

```
>>> help('modules')
```

Note that the term is in quotes.  Python does not care about single or double quotes most of the time so long as there are quotes.  Google "style guide" for reasons other people care.  The 'topics' listing is nice as it somewhat covers the goal of this doc under "IMPORTING" and "NAMESPACES".

----

# Namespaces

Quotes from https://martinfowler.com/bliki/TwoHardThings.html

> There are only two hard things in Computer Science: cache invalidation and naming things.
> -- Phil Karlton

Adding a twist.

> There are 2 hard problems in computer science: cache invalidation, naming things, and off-by-1 errors.

One more turn.

> There are only two hard problems in distributed systems:
> 2. Exactly-once delivery
> 1. Guaranteed order of messages
> 2. Exactly-once delivery

Let us say you have a neat function.  It initializes the resources necessary to interact with a text file and provides an object from which the user can perform those interactions.  It makes sense to call it `open`.  But what about the other guy that wrote some fancy code to do similar but for network communication?  He also wants to call his function `open`.
With namespaces, this is not a problem.  When you run `import os`, one of the functions included is `open` but it is stored within the `os` namespace.  To use the function with the import statement provided, you would have to include the namespace; `os.open()`.  If you change the import line around to `from os import open`, then you can call it as simply `open()` but you'd have to explicitly rename any other imported `open` functions or import them such that they'd require the namespace on each call.
Personally, I prefer to import to the namespace level when I think about it (meaning there are plenty of examples where I don't do that).  This makes it trivial to know where a piece of code is defined just by looking at the call.  Granted, most IDEs provide a way to jump to the declaration so it isn't that important.  Generally, it is beneficial to be consistent.  Google "style guide" for more on that.
Both directories and file names affect the namespaces that python uses.  As with most things, there are ways around that.  But for now, just know that if you have a file called `billy.py`, python will see things within it as `billy.function_name`.

For python's built-in help on namespaces, see:
```
>>> help('NAMESPACES')
```

----

# Importing builtins

A "builtin" is just some code that is included with python by default - it is "built in".  There's actually a builtins.py in python.  To see a list of the available modules you can import without having to pip install anything, use the help function mentioned earlier.

```
>>> help('modules')
``` 

This displays a multi-column list of modules you can import.  Some of the ones I most often use are:

* os - mostly for getting to environment variables `os.environ.get('VAR')`
* time - for adding delays to the execution `time.sleep(10)`
* pathlib - for messing around on the filesystem `pathlib.Path("folder").glob("*.txt")`
* re - regular expressions.  If you have a problem and you decide to solve it with regex, you now have 42 problems.

Neat thing:  At least on my machine, the column format is broken on the line that includes the 'formatter' module.

```
_struct             first               quopri              zipapp
_symtable           fnmatch             random              zipfile
_sysconfigdata__darwin_darwin formatter           re                  zipimport
_testbuffer         fractions           readline            zlib
_testcapi           ftplib              reprlib
```

Example time.  Let's import `time` so we can get some `sleep`.

```
>>> import time
```

Whew.  That was difficult.  We need some rest after that much work.  There's a `sleep` function in the `time` module that will let use rest for a bit.  But what if you do not know which function you needed?  You could either call help on the module, `help(time)`, or get a listing of the available functions, classes, and objects within the module.

\<aside><br />
I just noticed something odd.  On the command line, `ls` is used to get a listing of contents.  But in python, `dir` is used which is the same command Windows/DOS uses to get a listing of contents.  Anyways...<br />
\</aside>

Use the `dir()` function to get the list.

```
>>> dir(time)
```

And the output:

```
['CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID', 'CLOCK_REALTIME',
 'CLOCK_THREAD_CPUTIME_ID', 'CLOCK_UPTIME_RAW', '_STRUCT_TM_ITEMS', '__doc__', '__loader__',
 '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock_getres', 'clock_gettime',
 'clock_gettime_ns', 'clock_settime', 'clock_settime_ns', 'ctime', 'daylight', 'get_clock_info',
 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns',
 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time',
 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname', 'tzset']
```

The output is an object of type "list" of strings.  The sorting is alphabetical keeping in mind that all capital terms come before all lowercase terms and underscored terms are between the two groups.  Most of the time, you will be wanting something that starts with a lowercase letter so you can skip over the first two groups.  The general convention is all caps for constants or module-level variables, classes get initial caps and no underscores, functions and other variables get all lower with underscores between words.  As with any general convention, there are exceptions all over the place.

When I'm looking for something and don't feel like Googling it, I'll get the listing and poke at anything that looks promising.  In this case, `sleep` is the only function that looks like it would cause a delay.

As an alternative, you could browse the complete help for the module by using the module name without any function/class included - `help(time)`.  This will pop up a longer doc that is made up of the content you would see if you called help on each item in the `dir(time)` output.  It does have a little extra as it is module-level help, though.

Ok, we found the function that would add a delay but what kind of argument does it take?  Is it seconds or milliseconds?  Integer or decimal?  Call help to find out.

```
>>> help(time.sleep)
```

```
sleep(...)
    sleep(seconds)

    Delay execution for a given number of seconds.  The argument may be
    a floating point number for subsecond precision.
```

This output shows it takes a single argument that is the number of seconds and can be fractional.

So to sleep for 3.14 seconds but also check to see how long it takes, we use the `time` command (non-python) to time how long the full command takes.  Since there would be some overhead in starting up python, we first run it with nothing and subtract that time from the sleep time.

```
$ time python -c ""

real	0m0.138s
user	0m0.052s
sys	0m0.054s

$ time python -c "import time; time.sleep(3.14)"

real	0m3.278s
user	0m0.053s
sys	0m0.051s
```

The overhead run took 0.138 seconds and the sleep run took 3.278 seconds.  That actually works out to exactly 3.14 seconds for the `time.sleep` command.  This doesn't always happen as the overhead depends on what else is going on in the os.

----

# Importing Your File

Now, lets say you've created a script and want to test a function within the script.  You either need to set it up so it calls just what you want when executed as `python your_script.py` or you can import the script in the interactive prompt and call the function directly.

Importing a file actually executes the file.  Running the script as `python first.py` will have the following output.

```
This print is not inside of a function.
```

Now, go into the interactive prompt and import the script.  Note the extension is not included.  You will see a familiar line.

```
>>> import first
This print is not inside of a function.
```

Everything inside the file was executed when it was imported.  That doesn't mean the `print` function within the `hello` function was called as its output is not seen.  Instead, the `def hello(...` block was executed which _defines_ the `hello` function but does not _call_ it.  That means that you can now call `hello`.

```
>>> first.hello('the arg')
Hello.  You passed in the arg.
```

Because of how it was imported, you needed to specify the namespace.  You can change the import line a bit to avoid that.

```
>>> from first import hello
>>> hello('bob')
Hello.  You passed in bob.
```

When using the `from` style of import, you either need to specify each item you want imported or use the wildcard, `*`.  The wildcard will import anything in the given module or will be limited to what is in the `__all__` variable if it exists.  In `first.py`, there is an `__all__` which only lists two functions.  Here is the output of `dir()` showing what is getting imported each time.  The `[i for i in dir() if not i.startswith('_')]` bit is a "list comprehensions" which is a fancy way of saying a list is being built in one statement.  It isn't part of the topic of this doc and used here only to clarify the output.

With the `__all__` line:
```
$ python -c "from first import *; print([i for i in dir() if not i.startswith('_')])"
This print is not inside of a function.
['generic_func', 'hello']
```

Without the `__all__` line:
```
$ python -c "from first import *; print([i for i in dir() if not i.startswith('_')])"
This print is not inside of a function.
['dict_func_example', 'dict_func_example_a', 'dict_func_example_b', 'dict_func_example_c', 
 'dict_func_example_default', 'generic_func', 'hello', 'not_using_dict_func_example']
```

Personally, I stay away from wildcard imports.  It just feels unsafe.  If names of imported items are duplicated, conflicts will happen.  Not all conflicts will be immediately noticeable.  A function could be overwritten and slightly work if it is similar enough.

Importing using `from` means you need to be careful of other imports using the same name.  For the next example, the `second.py` file will also be used.  Both declare a function named `generic_func`.  If you import one and then the other, the second import will essentially overwrite the first.

```
>>> from first import generic_func
>>> generic_func()
generic_func() from first

>>> from second import generic_func
>>> generic_func()
generic_func() from second
```

This shows an important concept in how python deals with functions.  "Everything is an object" is a phrase I've heard somewhere but don't feel like looking up at the moment.  When a function is declared (the `def func_name()` line), what is happening is that an object named `func_name` is created with the value being the function body.  When the first `from/import` line is executed, the object `generic_func` is created and assigned the value as defined in `first.py`.  When the second `from/import` is executed, the existing `generic_func` object is overwritten and assigned the value from `second.py`.

To further show how functions are objects, you can assign functions to variables.  One pattern I've used and seen used numerous times is to create/build a dict where the values are all functions.  The functions which start as `dict_func_example` in `first.py` show a basic example of how this works.

```
>>> first.dict_func_example('absolute')
dict_func_example_a(absolute)

>>> first.dict_func_example('best')
dict_func_example_b(best)

>>> first.dict_func_example('contraption')
dict_func_example_c(contraption) 

>>> first.dict_func_example('hello')
no function matches. hello
```

The general idea is to use some key to determine which function needs to be called.  If you are familiar with `switch` or `case` statements in other languages, this works in a slightly similar manner.

Side tracking a little to cover some details used in this example.

## The dict object
A dict is a dictionary object.  It is made up of key/value pairs.  The keys can be any mix of "hashable types".  In general, strings, numbers, and tuples of strings and numbers are all I've used as keys.  The values can be anything from other strings and numbers to other dicts, functions, or objects.
A dict is declared by using the curly braces and colons, `{'key1': 'value1', 'key2': 'value2'}`.  Keys can be added or removed after the initial declaration.  The dict is not immutable.  Not much in python is immutable.  Adding a key can be done by assigning a value to it, `a_dict_var['new key'] = 'some value'`.
Getting a value from a dict can be done using the square brackets the same way, `print(a_dict_var['new key'])`.  A caveat of using the square brackets is if the key does not exist in the dict, a `KeyError` will be raised.  If that error is not handled by your code, the program will crash.
The `.get()` function on a dict is a way to safely get a value from a dict when you are not certain the key exists.  The `.get()` function takes one required argument and one optional argument for the default if the key does not exist.  In the `dict_func_example` function, if the desired key is not in the dict, the function `dict_func_example_default` is returned and assigned to `func`.

## Square Brackets
We've already covered one use for assigning and retrieving values in a dict.  Square brackets are used whenever an object can be indexed(or subscriptable).  As in, a list, tuple, set, dict, string, and others I'm likely forgetting.  You can add the ability for custom classes to handle square brackets by implementing the `__getitem__` function.
For lists, strings, tuples, and sets, the square brackets take an integer as the key.  The first element is 0 and the count goes up by one from there.  In the example function, the first character of the argument is found by `arg[0]`.  The function makes no attempt to validate the argument so it can easily be broken by passing in any value that is not subscriptable.
There's a whole pile of details not covered here.  Google "python list slicing" for more.

## String Formatting
One handy shortcut that has not been covered yet but already used is "f strings".  This is a relatively new feature which makes for some shorter lines.  The following print statements all produce the same output.

```
some_variable = "ipsum dolor"
another_variable = "consectetur adipisicing"

print("Lorem %s sit amet, %s elit" % (some_variable, another_variable))

print("Lorem {} sit amet, {} elit".format(some_variable, another_variable))

print("Lorem {1} sit amet, {0} elit".format(another_variable, some_variable))

print("Lorem {a} sit amet, {b} elit".format_map({'a': some_variable, 'b': another_variable}))

print(f"Lorem {some_variable} sit amet, {another_variable} elit")
```

In general, the first two prints use positional placeholders - the first `%s` or `{}` is replaced by the first argument following the string and so on.  The third print is similar but the number in the braces corresponds to the index of the argument with 0 being the first argument after the string.  That helps if you want to repeat a value in the string, you can have "{1} {1} {0} {1}" which would repeat the '1' arg three times and the '0' arg once.  The fourth print uses a dict as the arg where the keys act as the placeholders in the string.  If the string has a placeholder that does not exist in the dict, a KeyError will be raised.  You can create your own object that implements the `__missing__` function to get around KeyErrors, though.
The last is probably the most recommended as it just makes a pile of sense.  First, prefix the string with an 'f'.  Then, use existing variables for the placeholders.  You can call functions within the placeholders as well.  To force a string lowercase, `f"lowercase example: {variable.lower()}."`.  Essentially, whatever can be done in one expression can be done as the replacement.  The replacement happens on assignment of the string.  As in, if the f-string is assigned to a variable but not printed until later and after some replacement values have changed, the replacements already occurred on the assignment and won't reflect the changes.

```
>>> x = 1
>>> x_str = f"x is {x}"
>>> x = 3
>>> print(x_str)
x is 1
```

And now, back to fun with importing.

Back to the `dict_func_example` function.  It creates a dict named `pick_one`.  The keys are single characters and the values are three example functions.  Note that these are just the function names and do not have the parenthesis.  Without the parens, the functions are not yet called.
To pick the appropriate function, the first character of the variable `arg` is used in the call to `.get()`.  If that character is not a key in `pick_one`, the function `dict_func_example_default` is used.  Again, no parens on the functions being used just yet.
Now that a function has been assigned to the variable `func`, it can be called as if we were calling it by name.
This pattern is useful when <insert reasonable use-case here>.  An alternative to using this pattern is shown in `not_using_dict_func_example`.  This uses `if/elif/else` to pick and execute the appropriate function.  An advantage the dict pattern has is the dict could be generated at runtime while the `if/elif/else` is static.

# Importing Sibling File From Your File

Importing from one file to another in the same directory is done just as any other import.  Use the filename without the extension.  For example, in `sibling_first.py`, you would import `sibling_second.py` as, `import sibling_second`.  This would import the namespace `sibling_second` as the contents of `sibling_second.py`.  To access any of the items in `sibling_second`, the namespace needs to be used.  Functions of the same name would not conflict because of how the import was worded.  If the import was worded as `from sibling_second import same_name_func`, just the one function would be imported.

> Note: Bad practice in example.  Do not do both kinds of imports to the same module in the same file.  This is done in sibling_first.py to show how each behaves.

Running `python sibling_first.py` produces the following output.

```
[not-in-a-function] sibling_second.py loaded.
The call to calls_something_in_second() failed because the function hasn't been defined yet.
calling 'same_name_func()'
This comes from sibling_first.py
calling 'sibling_second.same_name_func()'
This comes from sibling_second.py
[not-in-a-function] sibling_first.py loaded.
```

First thing to note is order the not-in-a-function print statements executed.  Python runs a script line-by-line.  It doesn't even look at following lines before executing earlier lines.
The first line in the file is importing `sibling_second.py`.  All lines in that file are executed which is seen by the output of the not-in-a-function print statement at the end of the file.  This means the second line in `sibling_first.py` would be able to access the `sibling_second` namespace.  Notice that the second import does not result in another not-in-a-function print statement from `sibling_second.py`.  Python is smart enough to know it already imported the file so reuses the bits in memory and just picks out the `same_name_func` from the `sibling_second` namespace and adds it to the current namespace.
The try/except block is then run which shows the sequential nature of how a script is executed.  The function being called is defined in the file but it hasn't been defined yet.  This only applies to function calls outside of any function/class definition.  It is perfectly valid for a function to call another that is defined later in the same file.  The problem comes when a statement is executed that tries to execute something that isn't yet there.  A try/except block was used to show this in `sibling_first.py` so the execution would not be interrupted.
The definition of the next couple of functions produce no output but create the functions in the current namespace.  
The same function that was attempted in the try/except block is called again.  This time, it has been defined so it doesn't fail.  First, it calls the function from the current namespace and then from the `sibling_second` namespace.  Even though the second import line imports the function from that namespace into the current one, the output shows the function executed was the one from `sibling_first`.  This is because the definition of `same_name_func` in `sibling_first` came after the import and overwrote the definition in the current namespace.  If the second import line were moved to after the `def same_name_func():` block, the output would show the function from `sibling_second` was called.
The second call to `same_name_func` explicitly uses the namespace in the call so there is no question which function to use.
Finally, the not-in-a-function print statement from `sibling_first` is executed.

Usually, you would pay close enough attention to not import an object just to create one of the same name.  Pycharm does not seem to flag this as I thought it would.  It does flag calling a function before it is defined, so that is one error that should be trivial to avoid.


# Circular imports
Bad.  Avoid this.  This is when one file imports another file which then imports another file which imports another eventually importing the first file again.  Python will flag this as an some error as shown below.  Sometimes it will be ImportError and other times it will be AttributeError.  To see this output, run `python circular_a.py`.

```
This is a
Traceback (most recent call last):
  File "circular_a.py", line 1, in <module>
    import circular_b
  File ".../importing/circular_b.py", line 1, in <module>
    import circular_c
  File ".../importing/circular_c.py", line 1, in <module>
    import circular_a
  File ".../importing/circular_a.py", line 9, in <module>
    circular_b.func_b()
AttributeError: partially initialized module 'circular_b' has no attribute 'func_b' (most likely due to a circular import)
```

This tends to pop up mostly when using frameworks.  There have been times that I'd try to use some neat function I wrote in one module from another module only to find out that the framework imported things such that it caused problems.  Generally, it means some functions/classes/objects are not in the ideal locations to follow the convention set up by the framework.  Thankfully, it doesn't often occur.  It just happens often enough I felt an example was warranted.

# Adding directory structures

So far, the files have been in a flat namespace.  Everything has been at one level.  For sufficiently large projects, there would be groupings that would make sense to isolate.  Such as a group of modules all related to database access, another couple of groups related to file access and socket communication, and a final group for general utility functions.  At the first level within a group, the functions/classes/etc would likely be quite generic for the topic.  Going another folder level in would bring in some more specialized objects.  Bad car analogy: 1st level in would be a book on automobiles.  Next level in would be a book on cars (or trucks, vans, SUVs).  Next level in would be a book on luxury cars (or racing, cheap, off-road).

Python uses a file named `__init__.py` to let it know the folder is supposed to be treated as a package.  This allows you to have folders in your project that python knows it doesn't have to worry about.  Many times, these files will be empty and just there to make python happy.  Every folder in a package's structure needs to have its own `__init__.py` file.

The example files for this section are in the `structure` folder.
Quick new thing: running python with the `-c` option allows running a short script without a file and without dealing with the interactive prompt.  "Short", in this case, is only because typing a long script as a one-line command would be silly.

```
$ python -c "import structure; structure.run_all()"
```

This just imports the first folder in the example and calls a function.  That function imports files from other folders and calls various functions.  The output is a pile of print statements that show the actual order the various files are imported.  Also serves as another example that the files are actually executed when imported.

```
/structure/__init__.py starting
/structure/io/__init__.py starting
/structure/io/__init__.py ending
/structure/io/db/__init__.py starting
/structure/io/db/structure_db_1.py starting
/structure/io/db/structure_db_1.py ending
/structure/io/db/structure_db_2.py starting
/structure/io/db/structure_db_2.py ending
/structure/io/db/__init__.py ending
/structure/io/file/__init__.py starting
/structure/io/file/structure_file_1.py starting
/structure/io/file/structure_file_1.py ending
/structure/io/file/structure_file_2.py starting
/structure/io/file/structure_file_2.py ending
/structure/io/file/__init__.py ending
/structure/io/socket/__init__.py starting
/structure/io/socket/__init__.py ending
/structure/io/socket/structure_socket_1.py starting
/structure/io/socket/structure_socket_1.py ending
/structure/io/socket/structure_socket_2.py starting
/structure/io/socket/structure_socket_2.py ending
/structure/util/__init__.py starting
/structure/util/__init__.py ending
/structure/__init__.py ending
run_all() starting
db root-level function
db open
db run a query
file root-level function
file open
file move file function
the socket.function_at_root_module_level is not accessible because of how the imports are written.
socket open
socket do something.
first call that has an import
util root-level function
/structure/util/general_func.py starting
/structure/util/general_func.py ending
util commonly_useful_function
second call that has an import
util root-level function
util commonly_useful_function
run_all() ending
```

Breaking the output into a few steps.  The first step is from the initial `import structure` statement.  All of the first lines that start with `/structure/` are from that one import.  Each of the files include starting and ending print statements.  Compare the prints from the file and socket folders.  (blank line added for clarity)

```
/structure/io/file/__init__.py starting
/structure/io/file/structure_file_1.py starting
/structure/io/file/structure_file_1.py ending
/structure/io/file/structure_file_2.py starting
/structure/io/file/structure_file_2.py ending
/structure/io/file/__init__.py ending

/structure/io/socket/__init__.py starting
/structure/io/socket/__init__.py ending
/structure/io/socket/structure_socket_1.py starting
/structure/io/socket/structure_socket_1.py ending
/structure/io/socket/structure_socket_2.py starting
/structure/io/socket/structure_socket_2.py ending
```

While the import lines for the two folders is different, one imports the folder and the other imports specific files within, the main difference is in how the `__init__.py` file in each folder treats its siblings.  For `file`, the `__init__.py` imports the functions from the two sibling files.  In `socket`, the `__init__.py` does not import anything from its siblings.  Even though the import line in `structure.__init__.py` seems like it is skipping over the `__init__.py` in `socket`, it is still executing it.  The function in that `__init__.py` is not accessible, though.
Because the `__init__.py` in `file` imports its siblings, the print statements in those files show up before the `__init__.py`'s ending print statement.  The "point of execution" follows along the various files when the statements are executed - it doesn't finish with one file completely and move on to the next.

The next interesting bit is a function which has an import statement inside it.  The function in `util/__init__.py` has an import for the `util/general_func.py` file.  This import statement is not executed when the `__init__.py` is imported because it is within a function and the function was not executed; only defined.

```
first call that has an import
util root-level function
/structure/util/general_func.py starting
/structure/util/general_func.py ending
util commonly_useful_function
second call that has an import
util root-level function
util commonly_useful_function
```

The import statement within the function is executed only when the point of execution gets to it.  Once it does, the `/structure/...` print statements are executed as expected.  Then the function is called again, the import statement does not generate any output as python knows the file is already loaded.  There is a way to reimport modules, though.  So far, I've only used that feature in two places.  One of those is arguably not the best way.

Use case #1: Plugins.  Imagine a folder where all of the files are inspected and imported if they meet a certain criteria at runtime.  This would allow adding/removing features without having to change any surrounding code.  As I said, arguably not too useful as a list of module names could be all that needs changed.

Use case #2: Interactive testing.  For simple modules, manually testing some features in the interactive prompt can be useful.  At times, I'll end up with a pile of variables and defined functions in the prompt so stopping and restarting it would be a hassle.  Having the option to reload the module to incorporate changes makes life easier.
The basic flow would be (abbreviating because this is feeling very much like a tangent):

```
>>> import importlib
>>> import structure
>>> structure.func()
bad output

# make changes to structure/__init__.py

>>> importlib.reload(structure)
/structure/__init__.py starting
CHANGED
/structure/__init__.py ending
<module 'structure' from '.../structure/__init__.py'>

>>> structure.func()
good output
``` 

One important bit to be aware of: reloading a module does not force a reload of any modules it imports.  In the above example, I made a change to the root `/structure/__init__.py` by adding a print statement after its import lines.  Note that the starting/ending print statements only has a single line between them this time whereas they had almost 20 lines before.  This is because the reload function only reloads what it is explicitly told to.
Also, to be able to reload something, it needs to be imported as a file.  I've not found a way to reload a module that only had a few bits imported.  As in `from some_file import func`, the `some_file.py` has a function `func` imported but not the entire module.  Trying to reload `some_file` will result in "NameError: name 'some_file' is not defined" and trying it on `func` will result in "TypeError: reload() argument must be a module".  Trying `some_file.func` also results in a NameError.
Given all that, I've rarely used it.  So the above few paragraphs are somewhat pointless.

## Summary

* Imports are executed like any other statement - in the order they show up.
* Circular imports generally mean the function/class/file organization needs revisited.
* Folders allow grouping files into logical segments.  The deeper the folders, the more specialized.   
* `__init__.py` is needed in every folder of a package.


# Running a module

Not sure how this is related to importing but I added it to the list earlier so here we go.

There is a command line option on python which allows running a module directly.  Some of the builtin modules include such for whatever reasons.  One that I've used numerous times is in `http.server`.  This will start a simple HTTP server in the current folder.  This server doesn't do much other than serving up the files in the folder.  It can do some cgi (running scripts/executables) but I've not had it do so.

```
$ python -m http.server
```

Starting this in the folder with the example files will allow anyone on the network to see the files.  The generated web page will be a very basic file listing allowing the user to click on the files to see their content.  I've mainly used this to test some simple static pages - mostly css/javascript debugging.  There are further options to limit the address and port used and for specifying the hosted directory.

# Building your own runnable module

Lets say you want to allow a user to run some example code directly from the module.  In this completely made up example, we will add something to the `http.server` just so there's a lot of the interactivity already built in.

The goal is to have this command start with:

```
$ python -m custom_http
```

First step is to create the `custom_http.py` file and add in the bit that actually lets the `-m` option work.

```
if __name__ == '__main__':
    print("RUNNING!")
```

Having just those two lines will have python print "RUNNING!" when running the command show earlier.  The reason for the `if` block is so someone importing this file will not get the "RUNNING!" output.  In a more fleshed out example, the block would prevent a server from starting up when all that was wanted was an import.

A good place to start when you want to extend the functionality of something is the source code for that something.  To do so, we will use the "go to declaration" feature that is in most IDEs.  To do so, add the import line at the top of the file.

```
from http import server
```

Then, put the cursor on `server` and `cmd+B`/Navigate->"Declaration or Usages".  This should open a file named something like `python3.8/http/server.py`.  This is a file included with python.  Jump to the end of the file and page up a little.  You will see the start of an if block same as earlier (line 1262 in python 3.8.5).

For this little customization, we are going to not accept any command line arguments.  For a more useful tool, you'd likely add in most of these.  Since this is just an example, I'm keeping it simple.

The important bits are seeing that it is using the class `SimpleHTTPRequestHandler` on line 1282 and calling the `test` function on 1294.  The `DualStackServer` defined on 1286 is not familiar to me since the last time I've done this.  Just means a little more copy/paste to do.

The minimal amount of copied code is in `minimal_custom_http.py`.  The call to `test`, class definition `DualStackServer`, and a couple imports were all that needed to be copied.  By getting rid of the command line options, the address and port needed to be hard coded.

I got a little carried away with this example.  The `BogusHTTPRequestHandler` class ended up uglier than I wanted.  I believe what I had done on a previous customization was focused in the translate_path function which translates a url into a local file path.  I made it so certain urls were translated differently.  In this convoluted and overly complex example, I made one specific file show custom text instead of the file content.
This does work.  But it doesn't have much at all to do with the goal of this doc.