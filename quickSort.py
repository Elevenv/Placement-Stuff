#An array is divided into subarrays by selecting a pivot element
#elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.
# The subarrays are divided until each subarray is formed of a single element

def partition(arr,low,high):
    pivot = arr[high]
    i = low-1                                               #pointer for greater element
    
    # compare each element with pivot
    for j in range(low,high):
        if arr[j]<=pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    # swap the pivot element with the greater element specified by i
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quickSort(arr,low,high):
    if low<high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)                        # recursive call on the left of pivot

        quickSort(arr, pi+1, high)                       # recursive call on the left of pivot

arr = [8, 7, 2, 1, 0, 9, 6]
print(arr)
print(quickSort(arr, 0, len(arr)-1))
print(arr)


#Time Complexity O(n*log(n))
#space complexity O(log n)