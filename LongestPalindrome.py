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
# len1 = 0
# for k in pal:
#     if len(k)>len1:
#         len1 = len(k)
d = {}
for i in pal:
    d[len(i)] = i
# print(d)
# print(max(d))
# print()
# print(pal)
# print(max(pal))
print(d[max(d)])