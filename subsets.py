# https://leetcode.com/problems/subsets/

def Subset(nums):
    res = []
    subset = []

    def dfs(i):
        if i>=len(nums):
            res.append(subset.copy())
            print(subset,' appended')
            return
        
        subset.append(nums[i])              #decision to include nums[i]
        dfs(i+1)

        subset.pop()                        #decision not to include nums[i]
        dfs(i+1)
    
    dfs(0)
    return res

nums = [1,2,3]
print(Subset(nums))
