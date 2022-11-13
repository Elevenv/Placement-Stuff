# https://leetcode.com/problems/longest-substring-without-repeating-characters/

s = "abcabcbb"
# s = "pwwkew"
# s = "bbbbb"
# s= " "


ans = []
for i in range(len(s)):
    l = ''
    for j in range(i,len(s)):
        if s[j] not in l:
            l+=s[j]
        else:
            ans.append(len(l))
            break
    else:
        ans.append(len(l))

print(ans,max(ans))
