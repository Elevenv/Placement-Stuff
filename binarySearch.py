#To perform binary search array should be Sorted
#Divide and conquor 
#calculate mid and decide whether to check in right or left of mid

def binarySearch(arr,ele,low,high):
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == ele:
            return True
        elif ele>arr[mid]:
            low = mid+1
        else:
            high = mid-1
    return False
    
arr = [3, 4, 5, 6, 7, 8, 9]
print(binarySearch(arr, 7, 0, len(arr)-1))


#Time complexity    O(log n)
#Space Complexity   O(1)
