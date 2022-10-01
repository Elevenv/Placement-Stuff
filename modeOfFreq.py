nums = [5,9,2,9,7,2,5,3]
# nums = [5,9,2,9,7,2,5,3,1]
d = {}
for i in set(nums):
    d[i] = nums.count(i)
print(d)
ListVal = [i for i in d.values()]
ListVal.sort()
MaxMin = ListVal[0]
ans = 0
dValue = {}
for j in set(ListVal):
    dValue[j] = ListVal.count(j)

sub = dValue[ListVal[0]]
flag = True
for k in dValue:
    if sub-dValue[k]!=0:
        flag = False
        break
if flag:
    ans = min(list(dValue.keys()))
    print(ans)
else:
    listMax = max(list(dValue.values()))
    for k in dValue:
        if dValue[k]==listMax:
            print(k)
            break

# print('flag',flag)
# print(ListVal)
# print(dValue)
# print(ans)

# d = {2: 2, 3: 1, 5: 2, 7: 1, 9: 2}

d ={1: 1, 2: 2, 3: 1, 5: 2, 7: 1, 9: 2}
# nums = [5,9,2,9,7,2,5,3,1]
d2= {1:3,2:3,3:1}

# ct = 0
# ans = 0
# for i in d:
#     res = list(d.values()).count(d[i])
#     if res>ct:
#         ct = res
#         ans = res
# print(ans)
    # print(list(d.values()).count(d[i]))
# val =3
# for k in d2:
#     if d2[k]==val:
#         print(k)
#         break