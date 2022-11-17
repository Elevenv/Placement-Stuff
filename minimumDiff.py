# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

nums = [9,4,1,7]
k = 2
# nums = [87063,61094,44530,21297,95857,93551,9918]
# k = 6

nums.sort()
l = 1000000

i = 0
k = k-1
while i<len(nums) and k<len(nums):

    if nums[k]-nums[i]<l:
        l = nums[k]-nums[i]
    i+=1
    k+=1

print(l)
