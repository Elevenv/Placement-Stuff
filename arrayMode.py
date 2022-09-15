arr = [5,9,2,9,7,2,5,3,1]
dict1 = {}
for i in arr:
    ct = arr.count(i)
    if ct>1:
        dict1[i] = ct
largestOcurance = max(dict1.values())
arr.clear()
for j in dict1:
    if dict1[j] == largestOcurance:
        arr.append(j)
print(min(arr))