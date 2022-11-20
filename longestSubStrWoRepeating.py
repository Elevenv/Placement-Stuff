# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# s = "abcabcbb"
# s = "pwwkew"
s = "aab"
# s= "dvdf"

i = 0
j = 0
l = []
sub = ''

while i<len(s) and j<len(s):
    if s[j] not in sub:
        sub+=s[j]
        j+=1
    else:
        l.append(len(sub))
        sub = ''
        i+=1
        j = i
l.append(len(sub))
print(l)

# OR

# ans = []
# for i in range(len(s)):
#     l = ''
#     for j in range(i,len(s)):
#         if s[j] not in l:
#             l+=s[j]
#         else:
#             ans.append(len(l))
#             break
#     else:
#         ans.append(len(l))

# print(ans,max(ans))