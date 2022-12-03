# https://leetcode.com/problems/unique-paths/

m = 3
n = 2
# m = 3
# n = 7

row = [1]*n

for i in range(m-1):
    aboveRow = [1]*n
    for j in range((n-2),-1,-1):
        aboveRow[j] = aboveRow[j+1] + row[j]
    row = aboveRow
print(row[0])