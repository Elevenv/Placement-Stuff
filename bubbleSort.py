# compares two adjacent elements and swaps them
#At the end of each iteration largest element get placed at last position 


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):             #i-1 = to avoid list out of bound & comparing last element with first one 
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
data = [-2, 45, 0, 11, -9]
print(bubbleSort(data))


#Worst time complexity = O(n^2)
#Worst space complexity = O(1)