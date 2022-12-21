import builtins

a = [1, 2, 3, 4]

def my_fun():
    return 1


if __name__ == "__main__":
    """
    The built-in function dir() is used to find out which names a module defines. 
    It returns a sorted list of strings
    Without arguments, dir() lists the names you have defined currently:
    """
    print(dir())

    """
    dir() does not list the names of built-in functions and variables. 
    If you want a list of those, they are defined in the standard module builtins:
    """
    print(dir(builtins))

    """
    Packages:
    go to read about this, pretty important, talk about how package import modules and __all__
    """