"""
Q1
in a list of number
there is only 1 number that appears odd times, rest appears even times
find that number
O(N) O(1)
"""
from typing import List


def evenTimeOddTimes(nums: List) -> int:
    eor = 0
    for n in nums:
        eor ^= n
    return eor

my_nums = [1,1,2,2,3,3,6,4,4,5,5,7,7,2,2,1,1,4,2,3,3,2,4]
print(evenTimeOddTimes(my_nums))

"""
Q2
in a list of number
there are 2 numbers that appears odd times, rest appears even times
find those numbers
O(N) O(1)
"""
def evenTimeOddTimes2(nums: List) -> tuple:
    eor = 0
    for num in nums:
        eor ^= num

    # eor = a ^ b
    # eor != 0
    # eor must has a position that value is 1
    right_most_one = eor & (~eor + 1) # standard way to get the right most bit
    only_one = 0
    for num in nums:
        if num & right_most_one == 1:
            only_one ^= num
    return only_one, eor ^ only_one

my_nums = [1,1,2,2,3,3,6,4,4,5,7,7,2,2,1,1,4,2,3,3,2,4]
print(evenTimeOddTimes2(my_nums))
