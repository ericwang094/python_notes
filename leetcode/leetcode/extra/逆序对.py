# 在一个数组中，左边的数如果比右边的大，则这两个数构成逆序对
# https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        return self.reverse_pair(nums, 0, len(nums) - 1)

    def reverse_pair(self, nums: List[int], start: int, end: int) -> int:
        if start == end:
            return 0
        mid = start + (end - start) // 2
        return (self.reverse_pair(nums, start, mid) +
               self.reverse_pair(nums, mid + 1, end) +
               self.merge(nums, start, mid, end))

    def merge(self, nums: List[int], start: int, mid: int, end: int) -> int:
        sum = 0
        temp = []
        l, r = start, mid + 1
        while l <= mid and r <= end:
            if nums[l] <= nums[r]:
                temp.append(nums[l])
                l += 1
            else:
                temp.append(nums[r])
                sum += mid - l + 1
                r += 1

        temp.extend(nums[l: mid + 1])
        temp.extend(nums[r: end + 1])
        nums[start: end + 1] = temp

        return sum

input = [7, 5, 6,6, 4]
# input = [1, 1, 1]
result = Solution().reversePairs(input)
print(result)