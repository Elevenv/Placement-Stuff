# https://leetcode.com/problems/set-matrix-zeroes/

# matrix = [[1,1,1],[1,0,1],[1,1,1]]

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

row = []
col = []

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end='\t')
        if matrix[i][j] == 0:
            if i not in row:
                row.append(i)
            if j not in col:
                col.append(j)   
    print('\n')


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i in row:
            matrix[i][j] = 0
        if j in col:
            matrix[i][j] = 0

print('\n\n')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end='\t')
    print('\n')