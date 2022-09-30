arr = list(map(int,input().split()))
k = int(input())
arr1 = []
for i in range(0,k):
    ele = arr.pop(len(arr)-1)
    arr1.append(ele)
arr1.reverse()
print(arr1+arr)
