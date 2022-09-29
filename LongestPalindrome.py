string = 'abcba'
stringList = []
for i in range(len(string)+1):
    for j in range(i):
        if len(string[j:i])>1:
            stringList.append(string[j:i])
pal = []
for i in stringList:
    if i == i[::-1]:
        pal.append(i)
d = {}
for i in pal:
    d[len(i)] = i
print(d[max(d)])
