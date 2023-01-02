# Given an array of integers nums, sort the array in ascending order and return 
# it. 
# 
#  You must solve the problem without using any built-in functions in O(nlog(n))
#  time complexity and with the smallest space complexity possible. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not 
# changed (for example, 2 and 3), while the positions of other numbers are changed (
# for example, 1 and 5).
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5 * 10⁴ 
#  -5 * 10⁴ <= nums[i] <= 5 * 10⁴ 
#  
# 
#  Related Topics Array Divide and Conquer Sorting Heap (Priority Queue) Merge 
# Sort Bucket Sort Radix Sort Counting Sort 👍 3095 👎 591
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def selection_sort(self, nums):
        """
        The selection sort algorithm sorts an array by
        repeatedly finding the minimum element (considering ascending order)
        from unsorted part and putting it at the beginning.
        The algorithm maintains two subarrays in a given array.

        Time Complexity O(n^2)
        Space O(1)

        note: selection sort will fail the OC

        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            min_index = i
            for j in range(i+1, len(nums)):
                min_index = min_index if nums[min_index] < nums[j] else j
            nums[min_index], nums[i] = nums[i], nums[min_index]
        return nums

    def bubble_sort(self, nums):
        """
        :param nums:
        :return:

        Bubble sort is a sorting algorithm that
        compares two adjacent elements and swaps them until
        they are in the intended order.

        Time Complexity O(n^2)
        space O(1)
        """
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    def heapSort(self, nums):
        def heapify(nums, n, i):
            l = 2 * i + 1
            r = 2 * i + 2

            largest = i
            if l < n and nums[largest] < nums[l]:
                largest = l

            if r < n and nums[largest] < nums[r]:
                largest = r

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]

                heapify(nums, n, largest)

        n = len(nums)

        for i in range(n // 2 + 1)[::-1]:
            heapify(nums, n, i)

        for i in range(n)[::-1]:
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)
        return nums

    def insertion_sort(self, nums: List[int]) -> List[int]:
        # we don't need to start from 0 because 0 is already sorted
        for i in range(1, len(nums)):
            key = nums[i]

            # move elements of nums[0..i-1] that
            # are greater than key
            j = i - 1
            while (j >= 0 and key < nums[j]):
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
            return nums

    def merge_sort(self, nums: List[int]) -> List[int]:
        """
        Time complexity O(nlogn)

        :param nums:
        :return:
        """
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid: len(nums)])
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
    def sortArray(self, nums: List[int]) -> List[int]:
        """
                :type nums: List[int]
                :rtype: List[int]
                """
        # return self.selection_sort(nums)
        return self.heapSort(nums)
        
# leetcode submit region end(Prohibit modification and deletion)
