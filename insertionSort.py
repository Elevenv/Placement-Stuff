#divides array in two parts ie sorted and unsorted
#pick one element from unsorted list and add it in sorted list at its proper position

def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp          # Place key at after the element just smaller than it.
    return arr

arr = [9, 5, 1, 4, 3]
print(insertionSort(arr))


#Time Complexity O(n^2)
#Space complexity O(1)