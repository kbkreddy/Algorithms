# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        ret = res
        carry = 0
        while l1 or l2 or carry==1:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            total = first +second + carry
            carry = total //10
            total = total % 10
            print(total)
            res.next = ListNode(total)
            if l1:
                l1 = l1.next
            if l2:

                l2 = l2.next
            res = res.next

        return ret.next

        
            

            

        