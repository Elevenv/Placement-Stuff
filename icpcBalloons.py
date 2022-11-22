# https://www.codechef.com/problems/BALLOON

arr = [7,4,3,5,6,1,8,2,9,10,11]
# arr = [1,2,3,4,5,6,99,9,7]


arr = [8 ,7 ,6 ,5 ,4 ,3 ,2 ,1]
ct = 0
for i in range(len(arr)):
    if arr[i]>=1 and arr[i]<=7:
        ct+=1
    if ct == 7:
        break
print(i+1)


# OR


# l = [1,2,3,4,5,6,7]
# ct = 0

# for i in range(len(arr)):
#     if l:
#         if arr[i] in l:
#             l.remove(arr[i])
#         ct+=1

# print(ct)
