# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 215. Kth Largest Element in an Array


nums = [3,2,3,1,2,4,5,5,6]
k = 4

# nums.sort()
# res = len(nums)-k
# print(nums[res])

# OR

nums.sort()
nums.reverse()
print(nums[k-1])