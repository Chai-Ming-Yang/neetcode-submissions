# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ pre1, pre2 """
        li1, li2 = l1, l2
        carry = 0
        cur = dummy = ListNode()
        while li1 and li2:
            total = li1.val + li2.val + carry
            carry = total // 10
            total %= 10
            cur.next = ListNode(total)
            cur = cur.next
            li1, li2 = li1.next, li2.next
        while li1:
            total = li1.val + carry
            carry = total // 10
            total %= 10
            cur.next = ListNode(total)
            cur = cur.next
            li1 = li1.next
        while li2:
            total = li2.val + carry
            carry = total // 10
            total %= 10
            cur.next = ListNode(total)
            cur = cur.next
            li2 = li2.next
        
        if carry:
            cur.next = ListNode(carry)

        return dummy.next