# https://leetcode.com/problems/longest-common-prefix/submissions/
# 14. Longest Common Prefix


# strs = ["flower","flow","flight"]

# strs = ["dog","racecar","car"]

# strs = ["flower","flower","flower","flower"]

strs = [""]

# if len(strs)==0:
#     print('')
# if len(strs)==1: 
#     if strs[0]=='':
#         print('')
#     else:
#         print(strs[0][:1])
# comPrefix = []
# j = 1
# for i in range(len(strs)):
#     pre = strs[0][:j]
#     print(pre)
#     if i!=0:
#         if strs[i][:j]!=pre:
#             break   
#         if pre:
#             comPrefix.append(pre)
#             print('appended')
#         j+=1
# print(comPrefix)
# if comPrefix:   
#     print(max(comPrefix))

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