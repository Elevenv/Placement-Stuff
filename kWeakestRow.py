# mat = [
#     [1,1,0,0,0],
#     [1,1,1,1,0],
#     [1,0,0,0,0],
#     [1,1,0,0,0],
#     [1,1,1,1,1]
# ]

# countDict = {}
# for i in range(0,len(mat)):
#     count = 0
#     for j in range(0,len(mat[0])):
#         if mat[i][j] == 1:
#             count += 1
#     countDict[i] = count

# dict1 = dict(sorted(countDict.items(), key=lambda item: item[1]))
# k = int(input())
# finalList = []
# for i in range(0,k):
#     finalList.append(list(dict1.keys())[i])
# print(finalList)


# from hashlib import new
# from multiprocessing.dummy import Array


class Solution:
    def kweak(self,mat):
        countDict = {}
        for i in range(0,len(mat)):
            count = 0
            for j in range(0,len(mat[0])):
                if mat[i][j] == 1:
                    count += 1
            countDict[i] = count

        dict1 = dict(sorted(countDict.items(), key=lambda item: item[1]))
        k = int(input())
        k=3
        finalList = []
        for i in range(0,k):
            finalList.append(list(dict1.keys())[i])
        return finalList
    
    def acceptMatrix(self):
        row = 5
        col = 5
        mat = []
        for i in range(0,row):
            submatrix = []
            for j in range(0,col):
                submatrix.append(int(input()))
            if i != row-1:
                print("Next Row ")  
            mat.append(submatrix)
        return mat

if __name__=='__main__':
    ans = Solution()
    mat = ans.acceptMatrix()
    print(ans.kweak(mat))