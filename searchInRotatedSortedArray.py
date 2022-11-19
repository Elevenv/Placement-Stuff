nums = [4,5,6,7,0,1,2]
# nums = [1]
target = 0

l = 0
r = len(nums)-1

while l <= r:
    mid = (l+r)//2
    # print(mid)
    if target == nums[mid]:
        print(mid)
        break
    if nums[mid] >= nums[l]:
        if nums[l] <= target <= nums[mid]:
            r = mid
        else:
            l = mid+1	
    else:
		# Checking if target belongs to the sorted subarray
        if nums[mid] <= target <= nums[r]:
            l = mid
        else:
		    # else we will go to left part of array leaving middle too as arr[mid] != target
            r = mid-1
        
else:
    print(-1)

