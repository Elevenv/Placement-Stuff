# https://leetcode.com/problems/valid-anagram/

s = "anagram"
t = "nagaram"

# ss = sorted(s)
# tt = sorted(t)
# print(ss)
# print(tt)
# print(ss == tt)

# OR

for i in s:
    if i not in t:
        print(False)
        break
else:
    d = {}
    d1 = {}
    for j in s:
        if j in d:
            d[j]+=1
        else:
            d[j] = 1
    
    for k in t:
        if k in d1:
            d1[k]+=1
        else:
            d1[k] = 1
    flag = True
    for l in d:
        if d[l]!=d1[l]:
            flag = False
    print(flag)
    