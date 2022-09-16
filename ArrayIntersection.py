# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# 350. Intersection of Two Arrays II


arr1 = [1,2,2,1]
arr2 = [2,2]

# arr1 = [4,9,5]
# arr2 = [9,4,9,8,4]

commonEle = []
if len(arr1)>len(arr2):
    largeArr = arr1
    smallArr = arr2
else:
    largeArr = arr2
    smallArr = arr1

for j in largeArr:
    if largeArr.count(j)==smallArr.count(j):
        commonEle.append(j)
    else:
        if j in smallArr:
            if j not in commonEle:
                commonEle.append(j)
print(commonEle)


