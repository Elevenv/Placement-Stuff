# https://leetcode.com/problems/longest-common-prefix/submissions/
# 14. Longest Common Prefix


# strs = ["flower","flow","flight"]

# strs = ["dog","racecar","car"]

strs = ["flower","flower","flower","flower"]

# strs = [""]


fList = []
j = 1
for i in range(len(min(strs))):
    flag = True
    pr = strs[0][:j]
    for k in strs:
        if pr!=k[:j]:
            flag =False
            # break
    if flag:
        fList.append(pr)
    j+=1
if fList:
    print(max(fList))
else:
    print('none')
