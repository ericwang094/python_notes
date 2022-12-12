# https://docs.python.org/3/tutorial/controlflow.html#function-examples

"""
the interesting part is the function arg / and *
in a function declaration, everything before / must be positional arg
while everything after * must be keyword-only, anything in between can be
either positional or keyword

def combined_example(pos_only, /, standard, *, kwd_only)
"""

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2) # 2

standard_arg(arg=2) # 2

pos_only_arg(1) # 1

pos_only_arg(arg=1) # throw error since arg is before / so it must be positional not key arg

kwd_only_arg(3) # throw error since arg is after *, so it must be key args

kwd_only_arg(arg=3) # 3

combined_example(1, 2, kwd_only=3) # 1 2 3

combined_example(1, standard=2, kwd_only=3) # 1 2 3

def foo(name, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2}) # will throw error,
                      # because name is already positional args,
                      # it is duplicate to have a key

# but we can do this
def foo(name, /, **kwds):
    return 'name' in kwds