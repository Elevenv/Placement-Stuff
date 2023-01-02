def MinMax(arr,k):
    for i in range(k):
        arr.remove(min(arr))
        arr.remove(max(arr))
    
    return sum(arr)/len(arr)


k = 3
arr = [2,435,433,2,23,2,823,5,835,45,4676,23,2,1,99,5,2,43,52]
# 2 9 -10 25 1
# arr.sort()
# print(arr)
print("%.6f"%MinMax(arr, k))
# arr.sort()
# print(arr)