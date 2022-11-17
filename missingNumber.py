# https://leetcode.com/problems/missing-number/


nums = [9,6,4,2,3,5,7,0,1]
# nums = [1]
# nums.sort()

# for j in range(len(nums)):
#     if j not in nums:
#         print(j)
#         break
# else:
#     print(len(nums))

# OR

nums1 = [i for i in range(len(nums)+1)]

print(sum(nums1)-sum(nums))