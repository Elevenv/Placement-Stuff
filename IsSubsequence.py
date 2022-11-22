# https://leetcode.com/problems/is-subsequence/

s = "abc"
t = "ahbgdc"

si = 0
ti = 0
ct = 0

while si<len(s) and ti<len(t):
    if s[si] == t[ti]:  
        si+=1
        ti+=1
        ct+=1
    else:
        ti+=1
print(True) if ct == len(s) else print(False)
print(ct)