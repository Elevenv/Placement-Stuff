# https://leetcode.com/problems/single-number/submissions/
# 136. Single Number 

nums = [4,1,2,1,2]
d = {}
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1

for j in d:
    if d[j]==1:
        print(j)


# OR 

# nums = [4,1,2,1,2]
# nums.sort()
# print(nums)
# flag = False
# i = 0
# while i<len(nums)-1:
#     if nums[i]==nums[i+1]:
#         i+=2
#     else:
#         print(nums[i])
#         flag = True
#         break
# if not flag:
#     print(nums[-1])