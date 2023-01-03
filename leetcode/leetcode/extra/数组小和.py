# 　数组小和的定义如下：
# 　　例如：数组s = [1, 3, 5, 2, 4, 6]，在s[0]的左边小于或者等于s[0]的数的和为0，
#     在s[1]的左边小于或等于s[1]的数的和为1……将所有位置的左边比它小或者等于的数的和相加起来就是小和。
# 　　给定一个数组，实现函数返回s的小和。
# 例子：
# [1,3,4,2,5]
# 1左边比1小的数， 没有；
# 3左边比3小的数， 1；
# 4左边比4小的数， 1、 3；
# 2左边比2小的数， 1；
# 5左边比5小的数， 1、 3、 4、 2；
# 所以小和为1+1+3+1+1+3+4+2=16
import random
from collections import Counter
from typing import List


def getSmallSum(arr: List[int]) -> int:
    def mergeSort(arr: List[int], start: int, end: int) -> int:
        if start == end:
            return 0
        mid = (start + end) // 2
        return mergeSort(arr, start, mid) + mergeSort(arr, mid + 1, end) + merge(arr, start, mid, end)

    def merge(arr: List[int], start: int, mid: int, end: int) -> int:
        left = start
        right = mid + 1
        res = []
        sum = 0
        while left <= mid and right <= end:
            if arr[left] < arr[right]:
                res.append(arr[left])
                sum += arr[left] * (end - right + 1)
                left += 1
            else:
                res.append(arr[right])
                right += 1
        res += arr[left: mid + 1]
        res += arr[right: end + 1]
        arr[start: end + 1] = res
        return sum

    if arr == None or len(arr) == 0:
        return 0

    return mergeSort(arr, 0, len(arr) - 1)


# Method 3
def test(nums: List[int]) -> int:
    if nums is None or len(nums) == 0:
        return 0

    return mm_sort(nums, 0, len(nums) - 1)

def mm_sort(nums: List[int], start: int, end: int) -> int:
    if start == end:
        return 0

    mid = start + (end - start) // 2
    return mm_sort(nums, start, mid) + mm_sort(nums, mid + 1, end) + mm_merge(nums, start, mid, end)

def mm_merge(nums: List[int], start: int, mid: int, end: int) -> int:
    left = start
    right = mid + 1
    res = []
    sum = 0
    while left <= mid and right <= end:
        if nums[left] < nums[right]:
            res.append(nums[left])
            sum += nums[left] * (end - right + 1)
            left += 1
        else:
            res.append(nums[right])
            right += 1
    res.extend(nums[left: mid + 1])
    res.extend(nums[right: end + 1])

    for i in range(start, end + 1):
        nums[i] = res.pop(0)
    return sum

# ac version
# python3 solution
def min_sum_entry(array):
    return min_sum(array, 0, len(array) - 1)
def min_sum(array, l, r):
    if l == r:
        return 0
    mid = l + (r - l) // 2
    l_min_sum = min_sum(array, l, mid )
    r_min_sum = min_sum(array, mid + 1, r)
    extra = merge(array, l, mid, r)

    return l_min_sum + r_min_sum + extra


def merge(array, l, m, r):
    """Merge sort."""
    res = 0
    # sorted array[l: r]
    temp = []
    i, j = l, m + 1
    while i <= m and j <= r:
        if array[i] < array[j]:
            res += array[i] * (r - j + 1)
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= m:
        temp.append(array[i])
        i += 1

    while j <= r:
        temp.append(array[j])
        j += 1

    array[l: r + 1] = temp

    return res

def main():
    # test_times = 500
    # max_value = 5000
    # max_elements = 500
    
    test_times = 1
    max_value = 5
    max_elements = 5

    list_a = [random.randint(0, max_value) - random.randint(0, max_value) for _ in range(max_elements)]
    list_a = [1, 3, 5, 2, 4, 6]
    list_b = list_a[:]
    print("test list: ")
    print(list_a)
    standard_result = min_sum_entry(list_a)
    my_result = getSmallSum(list_b)
    is_success = True
    for _ in range(test_times):
        if standard_result != my_result:
            print("result not the same")
            print(f"standard_result: {standard_result}")
            print(f"my_result: {my_result}")
            is_success = False
            break
    if is_success:
        print("result same")

if __name__ == '__main__':
    main()
