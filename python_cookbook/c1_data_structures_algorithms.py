# 1.1 unpacking
# if unpacking using *, it will always be list, even it
# only contains 1 element
record = ('Dave', 'abc', '4523423', '24523423')
name, email, *numbers = record
print(numbers)

# 1.4 heap
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # [42, 37, 23]
print(heapq.nsmallest(3, nums))  # [-4, 1, 2]

# order by custom key
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)  # yhoo, fb, hpq
print(expensive)  # aapl, acme, ibm

# heapify
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)

# 1.6 dict vs defaultdict
from collections import defaultdict
default_d = defaultdict(list)
default_d['a'].append(1)
default_d['b'].append(1)
default_d['a'].append(2)
print(default_d)

normal_d = {}
normal_d.setdefault('a', []).append(1)
normal_d.setdefault('a', []).append(2)
normal_d.setdefault('b', []).append(1)
print(normal_d)

# 1.9 find commonalities in two dictionaries
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}
# find keys in common
print(a.keys() & b.keys())  # {'x', 'y'}

# keys in a not in b
print(a.keys() - b.keys())  # {'z'}

# find (key, value) pairs in common
print(a.items() & b.items())  # {('y'), 2}

# 1.11 slice
# slice is useful if you want to avoid some hardcoded index
record = '....................100.......513.25..........'
cost = int(record[20:23]) * float(record[31:36]) # not good
SHARES = slice(20, 23)
PRICE = slice(31, 36)
new_cost = int(record[SHARES]) * float(record[PRICE])
print(new_cost)

# 1.13 sorting a list of dictionaries by a common key
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

# it also accepts multiple keys
multi_keys = sorted(rows, key=itemgetter('fname', 'lname'))
print(multi_keys)

# the itemgetter can be replaced by lambda, but itemgetter is a bit faster
rows_by_fname_lambda = sorted(rows, key=lambda r: r['fname'])
print(rows_by_fname_lambda)

#1.14 similar to itemgetter, we have attrgetter on object
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
users = [User(23), User(3), User(99)]
from operator import attrgetter
users=sorted(users, key=attrgetter('user_id'))
print(users) # [User(3), User(23), User(99)]

# 1.18 namedtuple
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)  # Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print(sub.addr) # jonesy...
print(sub.joined) # 2012
print(len(sub)) # 2
addr, joined = sub
print(addr)
print(joined)

# the benefit of using namedTupled is to reduce decouple the
# position of the elements it manipulates, for example, if you
# were using tuple to express db table, if you added a column,
# the tuple index would messed up, so as your code, example
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total
# better solution with namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

# !!! beware, unlike dict, namedtuple (and tuple) is immutable,
# if you need to change any attributes, need to use _replace(),
# it will make an entirely new namedtuple with specified values replace
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 111, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
