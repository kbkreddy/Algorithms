"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        map = defaultdict(Node)

        curr = head

        while curr:
            map[curr]= Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            child = curr.next
            random = curr.random

            new= map[curr]
            if child:
                new.next = map[child] 
            if random:
                new.random = map[random]

            curr= curr.next
            
        return map[head]


        