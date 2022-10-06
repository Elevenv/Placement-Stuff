# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,1,1]
# a = [2,1,5,3,10,6,9,7]

nums[:] = sorted(set(nums))
print(len(nums))

# for i in nums:
#     if nums.count(i)>1:
#         nums.remove(i)

# print(nums)