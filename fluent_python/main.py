my_list = list(range(10))
my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)

from collections import deque
deque = deque(range(10))
deque.rotate(3)
print(deque)

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
print(id(a),id(b))
print(a == b)

from collections import defaultdict
map = defaultdict()