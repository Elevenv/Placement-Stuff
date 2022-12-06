nums = [1,2,3]
subSet = [[]]
for i in range(len(nums)+1):
    for j in range(i):
        subSet.append(nums[j:i])

print(subSet)
# print(nums[1:1])  