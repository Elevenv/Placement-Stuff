# https://leetcode.com/problems/pascals-triangle/

def PascalTriangle(numRows):
    ans = [[1]]
    for i in range(numRows-1):
        temp = [0] + ans[-1] + [0]
        row = []
        for j in range(len(ans[-1])+1):
            row.append(temp[j]+temp[j+1])
        ans.append(row)
    return ans

numRows = int(input())
print(PascalTriangle(numRows))



# DP Solution

# c = [[1]*i for i in range(1,6)]
# for i in range(5):
#     for j in range(i):
#         if i==j or j==0:
#             c[i][j] = 1
#         else:
#             c[i][j] = c[i-1][j-1] + c[i-1][j]
# print(c)
