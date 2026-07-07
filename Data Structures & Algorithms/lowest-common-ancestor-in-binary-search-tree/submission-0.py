# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root:
            return TreeNode(101)

        if p.val == root.val:
            return p
        elif q.val==root.val:
            return q
        print(root.val)
    
        leftFind = self.lowestCommonAncestor(root.left, p, q)
        rightFind = self.lowestCommonAncestor(root.right, p, q)
        if leftFind.val!=101 and rightFind.val!=101:
            return root
        elif leftFind and rightFind.val ==101:
            return leftFind
        elif leftFind.val ==101 and rightFind:
            return rightFind
        else:
            return TreeNode(101)


        



        