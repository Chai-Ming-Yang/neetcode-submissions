# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        nex, newH = head.next, None
        while nex:
            head.next = newH
            newH = head
            head, nex = nex, nex.next
        head.next = newH
        newH = head

        return newH