arr = [10,20,30,40,50]
start,temp,end =0,0, len(arr)-1
for i in range(0,len(arr)):
    if start == end:
        break
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start+=1
    end-=1
print(arr)