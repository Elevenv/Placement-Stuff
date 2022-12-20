class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        min1 = 1
        for i in range(len(nums)):
            if nums[i]==min1:
                min1+=1
        return min1
