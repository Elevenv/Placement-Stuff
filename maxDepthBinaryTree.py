# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        stack = [[root,1]]
        res = 0
        
        while stack:
            node,depth = stack.pop()
            
            if node:
                res = max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return res

if __name__=='__main__':
    root = [3,9,20,None,None ,15,7]
    obj = Solution()
    print(obj.maxDepth(root))