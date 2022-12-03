# https://leetcode.com/problems/transpose-matrix/

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3],[4,5,6]]
n = len(matrix)
m = len(matrix[0])
transMat = [[0 for i in range(n)] for k in range(m)]

for i in range(n):
    for j in range(m):
        transMat[j][i] = matrix[i][j]

print(matrix)
print(transMat)