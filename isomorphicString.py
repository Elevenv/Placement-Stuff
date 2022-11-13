# https://leetcode.com/problems/isomorphic-strings/
#205. Isomorphic String

# s = "egg"
# t = "add"

s = "badc"
t = "baba"

if len(s)!=len(t):
    print(False)

d = {}
for (i,j) in zip(s,t):
    if j not in d.values():
        d[i] = j

print(d)
flag = True
for k in range(len(s)):
    if s[k] not in d:
        flag = False
        break

    if d[s[k]] != t[k]:
        flag = False
        break
print(flag)