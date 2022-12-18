# https://leetcode.com/problems/count-common-words-with-one-occurrence/description/


words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]

# s = 0
# for i in words1:
#     if words1.count(i)==1 and words2.count(i)==1:
#         s+=1

# OR

d = {}
d1 = {}

for i in words1:
    if i not in d:
        d[i] = 1
    else:
        del d[i]

for j in words2:
    if j not in d1:
        d1[j] = 1
    else:
        del d1[j]
s = 0

for i in d:
    if i in d1:
        s+=1
print(s)
