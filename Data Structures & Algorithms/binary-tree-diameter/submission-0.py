# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHei = self.maxHei(root.left)
        righthei = self.maxHei(root.right)
        dia = leftHei + righthei

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(dia, sub)       


    

    def maxHei(self, root):
        

        if not root:
            return 0
        right =  self.maxHei(root.right)
        left = self.maxHei(root.left)

        return max(right,left)+1


        