# https://leetcode.com/problems/word-pattern/
#290. Word Pattern


# pattern = "abba"
# s = "dog cat cat dog"

pattern = "abba"
s = "dog cat cat fish"

if len(pattern)!=len(s.split(' ')):
    print(False)

d = {}

for (i,j) in zip(pattern,s.split(' ')):
    if j not in d.values():
        d[i] = j

print(d)

for k in range(len(pattern)):
    if pattern[k] not in d:
        print(False)
        break
    if d[pattern[k]] != s.split(' ')[k]:
        print(False)
        break
else:
    print(True)