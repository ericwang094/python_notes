import functools
import numbers
import operator
from array import array
import reprlib
import math

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        # the following is slow
        # return tuple(self) == tuple(other)

        return len(self) == len(other) and all (a == b for a, b in zip(self, other))

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    # in order to support slice method, we need to implement __getitem__ and __len__
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        # the following implementation will return array not list
        # return self._components[index]
        cls = type(self)
        if isinstance(index, slice):
            print("in instance slice")
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            print("in instance number")
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = "xyzt"

    def __getattr__(self, name):
        # the getattr work as following:
        # check if my_obj instance has the attribute named as x
        # then, goes to the class and then up the inheritance graph
        # then, if x is not found, the __getattr__ method defined in the class of my_obj is called with self and the name of
        # the attributes as a string eg("x")
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = "readonly attribute {attr_name!r}"
            elif name.islower():
                error = "can't set attritubes 'a' t 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)

if __name__ == '__main__':
    v7 = Vector(range(7))
    print(v7[-1])
    print(v7[1:4])
    print(v7[1])

    # if we only have getattr, it will have problem as following, explaination is on page 286
    v = Vector(range(5))
    print(v)
    print(v.x) # this will print 0.0
    v.x = 10
    print(v.x) # print 10
    print(v) # but the v still 0.0