### 对数器
import math
import random
from typing import List, Callable


# 对数器 is a tool that you can compare two algorithm result
# For example, if you have 1 approach A, another approach B, both are doing sorting
# you implemented A but not sure, so what you can do is to generate random array
# large number of times and compare approachA and approachB

def selection_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        min_value = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] < min_value:
                min_value = nums[j]
                nums[j], nums[i] = nums[i], nums[j]
    return nums


def bubble_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


def insertion_sort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def merge_sort(nums: List[int]) -> List[int]:
    """
    Time complexity O(nlogn)

    :param nums:
    :return:
    """
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid: len(nums)])
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
    return nums
def generator_random_list(max_element: int, max_length: int) -> List[int]:
    return [random.randint(0, max_element) - random.randint(0, max_element) for _ in range(random.randint(0, max_length))]

def compare(selection_method: Callable):
    max_element = 100000
    max_length = 1000
    test_times = 500

    is_success = True
    for _ in range(test_times):
        list_a = generator_random_list(max_element, max_length)
        list_b = list_a[:]

        sort_a = selection_method(list_a)
        sort_b = sorted(list_b)
        if sort_a != sort_b:
            print(f"{selection_method} isn't right")
            print(f"sort_a: {sort_a}")
            print(f"natural sort: {sort_b}")
            is_success = False
            break
    if is_success:
        print(f"{selection_method} sort is right")

def main():
    sort_algos = [selection_sort, bubble_sort, insertion_sort, merge_sort]
    # sort_algos = [merge_sort]

    for sort_algo in sort_algos:
        compare(sort_algo)

if __name__ == '__main__':
    main()