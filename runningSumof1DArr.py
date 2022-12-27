class Solution:
    def RunningSum(self,nums):
        # ans = []

        # for i in range(1,len(nums)+1):
        #     ans.append(sum(nums[:i]))
        # return ans

    # OR
    
        ans = []
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            ans.append(sum)
            
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1,1]
    # nums = [1,2,3,4]
    print(s.RunningSum(nums))