# https://leetcode.com/problems/3sum/
# 15.3Sum

nums = [-1,0,1,2,-1,-4]
# nums = [0,0,0]
arr=[]
nums.sort()
for i in range(len(nums)):
    left=i+1
    right=len(nums)-1
    while left<right:
        if nums[i]+nums[left]+nums[right]==0:
            arr.append((nums[i],nums[left],nums[right]))
            left+=1
            right-=1
        elif nums[i]+nums[left]+nums[right]>0:
            right-=1
        else:
            left+=1
print(set(arr))