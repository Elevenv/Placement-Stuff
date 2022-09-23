# https://leetcode.com/problems/permutations/
# 46. Permutations

def permute(nums):
    result = []
    if len(nums)==1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result

nums = [1,2,3]
print(permute(nums))


# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]