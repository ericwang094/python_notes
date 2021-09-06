## list

* difference between sort and sorted

```python
# sort method will change the original list, while sorted maintain original list
my_list = [3,2,5,4,1]
print(sorted(my_list))
# [3,2,5,4,1]
print(my_list)


my_list.sort()
# [1,2,3,4,5]
print(my_list)

```

* given a num n print square of each number on a separate line.
```python
if __name__ == '__main__':
    n = int(input())
    print(*[_ ** 2 for _ in range(n)], sep='\n')
```

* given number n, print 123..n
```python
if __name__ == '__main__':
    n = int(input())
    print(*range(1, n+1), sep="")
```

* Copy a list, they are two separate lists
```python
my_list = [1, 2, 3]
new_list = my_list[:]
```

* tuple is immutable

* looping through map
```python
user_map = {
    "username": "eric",
    "pwd": "123",
    "age": 30
}
for key, value in user_map.items():
    print(key) 
    print(value)

for key in user_map.keys():
    print(key)

for value in user_map.values():
    print(value) 
```