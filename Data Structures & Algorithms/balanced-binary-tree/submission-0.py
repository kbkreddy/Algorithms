# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        if right == True and left == True and abs(self.getHeight(root.right)-self.getHeight(root.left))<=1:
            return True
        else:
            return False

        return True if abs(left-right)<=1 else False


    def getHeight(self, root):

        if not root:
            return 0
        
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        return max(left,right)+1
        