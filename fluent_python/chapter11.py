import collections.abc
import numbers


class TestClass(collections.abc.Sized):
    pass


my_bool = True
print(isinstance(my_bool, numbers.Integral))