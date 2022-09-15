# https://leetcode.com/problems/merge-sorted-array/
# 88. Merge Sorted Array


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
step = 0
for i in range(3,len(nums1)):
    nums1[i] = nums2[step]
    step+=1
nums1.sort()
print(nums1)