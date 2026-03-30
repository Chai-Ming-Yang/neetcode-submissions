# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lag = lead = dummy
        for _ in range(n):
            lead = lead.next
        while lead and lead.next:
            lead = lead.next
            lag = lag.next
        if lag and lag.next:
            tmp = lag.next
            lag.next = tmp.next
            del tmp.next
        else:
            del lag.next
        return dummy.next