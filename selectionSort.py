# selects the smallest element from an unsorted list
#After each iteration smallest element will come at front 

def selectionSort(arr):
    for i in range(len(arr)):
        Min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[Min]:                         #finding smallest element
                Min = j
        arr[i],arr[Min] = arr[Min],arr[i]               #swap value at the end of iteration 
                                                        #Smallest element will come at front after each iteration
    return arr

arr = [-2, 45, 0, 11, -9]
print(selectionSort(arr))


#same as Bubble sort
#Time Complexity O(n^2)
#Space Complexity O(1)          