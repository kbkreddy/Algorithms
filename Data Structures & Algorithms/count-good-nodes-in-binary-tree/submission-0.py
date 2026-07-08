# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0

        if not root:
            return 0

        def dfs(root, maxi):
            nonlocal count
            if not root:
                return 
            
            if root.val>=maxi:
                count +=1
            
            dfs(root.right, max(maxi,root.val))
            dfs(root.left, max(maxi, root.val))
        dfs(root, root.val)
        
        return count
        