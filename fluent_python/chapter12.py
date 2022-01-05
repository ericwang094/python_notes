import collections


class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


class A:
    def ping(self):
        print("ping A:", self)


class B(A):
    def pong(self):
        print("pong B:", self)


class C(A):
    def pong(self):
        print("pong C", self)


class D(B, C):

    def ping(self):
        super().ping()
        print('post-ping: ', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == '__main__':
    # subclass built-in type is Tricky in python, init method
    # inherited from dict will be ignored
    dd = DoppelDict(one=1)
    print(dd) # {'one': 1}
    dd['two'] = 2
    print(dd) # {'one': 1, 'two': [2, 2]}

    # Therefore, we should use collections.UserDict for our own dict
    dd2 = DoppelDict2(one=1)
    dd2['two'] = 2
    print(dd2) # {'one': [1, 1], 'two': [2, 2]}

    d = D()
    # following both point to C
    d.pong()
    C.pong(d)

    print(D.__mro__)
    print("after mro")
    print(d.ping())