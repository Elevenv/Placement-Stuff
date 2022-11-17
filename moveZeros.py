# https://leetcode.com/problems/move-zeroes/

nums = [0,1,0,3,12]
# nums = [0,0,1]
# print(nums)
# for j in nums:
#     if j==0:
#         nums.remove(j)
#         nums.append(j)
# print(nums)

# OR

left = 0
for right in range(len(nums)):
    if nums[right]:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
print(nums)