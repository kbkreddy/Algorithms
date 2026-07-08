# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = deque()
        if not root:
            return []
        
        d.append(root)
        res = [root.val]
        currlevel = []

        while d:
            curr = d.popleft()

            if curr:
                if curr.left:
                    currlevel.append(curr.left)
                if curr.right:
                    currlevel.append(curr.right)
            
            if not d and currlevel:
                res.append(currlevel[-1].val)
                d = deque(currlevel)
                currlevel = []
        
        return res

