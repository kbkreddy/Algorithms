# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        res = []

        while head:
            res.append(head)
            head = head.next
        new = ListNode()
        i=0
        j = len(res)-1
        final = new
        while i<j:
            new.next = res[i]
            res[i].next = res[j]
            new = res[j]
            new.next = None
            i+=1
            j-=1
        if i==j:
            new.next = res[i]
            res[i].next=None
        
        



        