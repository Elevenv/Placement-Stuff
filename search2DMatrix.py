# https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def Search(self,matrix,target):
        # for i in matrix:
        #     i.sort()
        #     low = 0
        #     high = len(i)-1

        #     while low<=high:
        #         # mid = low + (high-low)//2
        #         mid = (low+high)//2

        #         if i[mid] == target:
        #             return True
        #         elif i[mid]<target:
        #             low = mid+1
        #         else:
        #             high = mid-1
        # return False

        # OR

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 34
    s = Solution()
    print(s.Search(matrix,target))