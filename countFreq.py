l = [1,2,3,4,5,1,4,1,3]
# d = {}
# for i in l:
#     d[i] = l.count(i)
# print(d)

count = 0
ele = 4
for i in range(len(l)):
    if l[i]==ele:
        count+=1
print(count)