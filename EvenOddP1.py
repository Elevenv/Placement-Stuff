arr = [1,2,3,4,5,6,7,8,9,10]
oddList = []
evenList = []
for i in arr:
    if i%2==0:
        evenList.append(i)
    else:
        oddList.append(i)
print(evenList+oddList)