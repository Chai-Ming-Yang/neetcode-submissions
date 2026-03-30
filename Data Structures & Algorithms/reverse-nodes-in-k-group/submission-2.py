# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1st iteration (no-loop)
        # to re-assign head
        oldHead = head
        p, n, cur = None, head, ListNode()
        for _ in range(k):
            cur = n.next
            n.next = p
            p = n
            n = cur
        head = p

        while cur:
            tmp = cur
            for _ in range(k):
                if not tmp:
                    oldHead.next = cur
                    return head
                tmp = tmp.next
            
            nexOldHead = cur
            p, n = None, cur
            for _ in range(k):
                cur = n.next
                n.next = p
                p = n
                n = cur
            oldHead.next = p
            oldHead = nexOldHead
            
        return head