# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

""" reverse 2nd half of list """
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find 2nd half (fast & slow)
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse 2nd half of list
        pre, cur = None, slow.next
        slow.next = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        # reorder
        lag, lead = head, pre
        while lead:
            l, r = lag.next, lead.next
            lag.next = lead
            lead.next = l
            lag, lead = l, r
        return
            