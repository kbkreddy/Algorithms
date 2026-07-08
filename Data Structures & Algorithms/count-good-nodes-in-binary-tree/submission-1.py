# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        def dfs(root, maxi, count):
            if not root:
                return count
            
            if root.val>=maxi:
                count +=1
            
            count1 = dfs(root.right, max(maxi,root.val),0)
            count2 = dfs(root.left, max(maxi, root.val),0)
            return count + count1 + count2
        return dfs(root, root.val, 0 )
        