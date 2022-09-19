houses = [[3,7],[1,9],[2,0],[5,15],[4,30]]
# houses = [[1,2],[2,3],[3,1],[4,20]]
d = {}
for i in houses:
    d[i[0]] = i[1]
SortedDict = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
print(SortedDict)
fList = []
finalList = []
for j in SortedDict:
    fList.append(j)

print(fList)
finalList = fList[-2:]
finalList.sort()
print(finalList)

# d = {1:'a',3:'b',2:'c',5:'u'}
# print(d)
# print(d.items())