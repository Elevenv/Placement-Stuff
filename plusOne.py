# https://leetcode.com/problems/plus-one/
# 66.Plus One

digits = [1,2,3]
numStr = ''
for i in digits:
    numStr+=str(i)
numStr = str(int(numStr)+1)
finalList = []
for j in numStr:
    finalList.append(int(j))
print(finalList)