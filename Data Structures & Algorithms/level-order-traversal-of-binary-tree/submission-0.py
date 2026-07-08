# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        d = deque()

        d.append(root)
        if not root:
            return []
        res = [[root.val]]

        currlevel = []

        while d:
            curr = d.popleft()
            if curr:
                if curr.left:
                    currlevel.append(curr.left)
                if curr.right:
                    currlevel.append(curr.right)
            
            if not d and currlevel:
                res.append([item.val for item in currlevel])
                d = deque(currlevel)
                currlevel = []
            
        return res
        

