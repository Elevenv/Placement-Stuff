
# mat = [[1,2,3],[1,2,3],[1,2,3]]
mat = [[1,1,1],[1,1,1],[1,1,1]]

j = 0
ans = 0

for i in range(len(mat)):
    ans+=mat[i][j]
    j+=1

print("First Diagonal sum : ",ans)

ans = 0
j = len(mat[0])
for j in range(len(mat)):
    ans+=mat[i][j]
    j-=1

print("Second Diagonal sum : ",ans)
