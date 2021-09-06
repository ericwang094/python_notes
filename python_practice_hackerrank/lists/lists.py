# Link https://www.hackerrank.com/challenges/python-lists/problem

# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    N = int(input())

    my_list = []

    for _ in range(N):
        command_line_components = input().split(" ")
        if len(command_line_components) == 3:
            position = int(command_line_components[1])
            value = int(command_line_components[2])
            my_list.insert(position, value)
            continue

        command_key = command_line_components[0]

        value = 0
        if len(command_line_components) != 1:
            value = int(command_line_components[1])

        if command_key == 'print':
            print(my_list)
        elif command_key == 'remove':
            my_list.remove(value)
        elif command_key == 'append':
            my_list.append(value)
        elif command_key == 'sort':
            my_list.sort()
        elif command_key == 'pop':
            my_list.pop()
        elif command_key == 'reverse':
            my_list.reverse()



