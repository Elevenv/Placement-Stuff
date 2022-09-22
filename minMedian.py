a,b = map(int,input().split())
l1 = []
med = []
for i in range(0,a):
    subList = []
    for j in range(0,a):
        subList.append(int(input()))
    l1.append(subList)

for j in l1:
    sortedList = j
    sortedList.sort()
    if a%2==0:
        med.append(sortedList[int(a/2)-1])
    else:
        med.append(sortedList[int(a/2)])

sum = 0
for k in med:
    sum+=k
print("medians : ",med)
if sum<b:
    print("Min median is : ",min(med))
else:
    print("-1")