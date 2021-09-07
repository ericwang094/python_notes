class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def __contains__(self, key):
        return key in self.keys()

    def __setitem__(self, key, value):
        self[str(key)] = value

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2']) # print two
print(d[4]) # print four
print(d[1]) # throw error

print(d.get('2')) # print two
print(d.get(4)) # print four
print(d.get(1, 'N/A')) # print N/A

print(2 in d) # True
print(1 in d) # False