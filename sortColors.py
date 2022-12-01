# https://leetcode.com/problems/sort-colors/

def sortColors(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[j]<nums[i]:
                nums[i],nums[j] = nums[j],nums[i]


# nums = [2,0,2,1,1,0]
nums = [4,2,9,5,7,8,9,3,5,66,44,67,88,6,7]
print(nums)
sortColors(nums)
print(nums)