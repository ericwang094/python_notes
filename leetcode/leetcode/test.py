a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print(a)
print(b)

print(3 ^ 4)
print(4 ^ 3)
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

def selection_sort(nums):
    for i in range(len(nums) - 1):
       curr_min = nums[i]
       for j in range(i + 1, len(nums)):
           curr_min = nums[j] if nums[j] < curr_min else curr_min

    return nums

def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j + 1] = key