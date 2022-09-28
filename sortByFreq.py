List = [4, 2, 5, 8, 5, 2, 2, 4, 4, 4]          # output : [4, 4, 4, 4, 2, 2, 2, 5, 5, 8]   Persistance interview question

l1 = []
for j in range(len(List)):
    high = 0
    ele = 0
    for i in List:
        if List.count(i)>high:
            high = List.count(i)
            ele = i
    for l in range(high):
        l1.append(ele)

    for k in List:
        if ele in List: 
            List.remove(ele)
print(l1)

# OR

# d = {}
# for i in l:
#     d[i] = l.count(i)
# print(d)

# sDict = {k:v for k,v in sorted(d.items(),key=lambda item:item[1],reverse=True)}
# print(sDict)
# l1 = [(str(k)+',')*v for k,v in sDict.items()]
# print(l1)

