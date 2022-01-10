import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')


class Sentence_1:
    # why sequence are iterable?
    # when the interpreter need to iterate over an object x, it automatically calls for built-in iter(x) function.
    # it is doing following
    # 1. check whether the object implements __iter__
    # 2. if __iter__ is not implemented, but __getitem__ is implemented,
    # python creates an iterator that attempts to fetch
    # items in order, starting form index 0.
    # 3. If that fails, python raises TypeError, usually saying  object is not iterable
    # this is why all python sequence is iterable, they all implement __getitem__,
    # in fact the standard sequence also implement __iter__,
    # the special handling of __getitem__ exists for backward compatibility
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


class IsIterable:
    # an object is considered to be iterable as long as it implements the __iter__ method

    def __iter__(self):
        pass


class Sentence_2:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)

# Generator
class Sentence_3:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # generator function doesn't raise StopIteration, it simply exists when its done.
        # no need for a separate iterator class
        for word in self.words:
            yield word


class Sentence_4_lazy:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

        # or to use syntactic sugar
        # return (match.group() for match in RE_WORD.finditer(self.text))

# Difference between iterable and iterator:
# iterable have an __iter__ method the instantiates a new iterator every time
# Iterator implement a __next__ method that returns individual items, and an __iter__ method that returns self
class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == '__main__':
    sentence = Sentence_1('"The time has come," the Walrus said, ')
    for word in sentence:
        print(word)
    print(list(sentence))

    print(isinstance(IsIterable(), abc.Iterable))

    # test on iter
    s3 = Sentence_1("Pig and Pegger")
    it = iter(s3)
    print(it)

    print(next(it)) # Pig
    print(next(it)) # and
    print(next(it)) # Pegger
    # print(next(it)) # Throw StopIteration error

    print(list(it)) # []
    print(list(iter(s3))) # ['Pig', 'and', 'Pepper']

    # test on yield
    def gen_123():
        yield 1
        yield 2
        yield 3
        return

    for i in gen_123():
        print(i) # will print 1, 2, 3

    g = gen_123()
    next(g) # 1
    next(g) # 2
    next(g) # 3
    # next(g) # throw error

    # test on yield 2
    def gen_AB():
        print("start")
        yield "A"
        print("continue")
        yield "B"
        print("end")

    for c in gen_AB():
        print("-->", c)

    res1 = [x*3 for x in gen_AB()] # this will print start, continue, end directly
    for i in res1:
        # will print
        # AAA
        # BBB
        print("-->", i)

    # this will print
    # start
    # --> AAA
    # continue
    # --> BBB
    # end
    res2 = (x*3 for x in gen_AB())
    for i in res2:
        print("-->", i)