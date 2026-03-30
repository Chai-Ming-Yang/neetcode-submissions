# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        heap 
        hashmap
        """
        head = cur = ListNode()
        h = []

        for i, node in enumerate(lists):
            if list:
                heapq.heappush(h, (node.val, i, node))

        while h:
            _, i, node = heapq.heappop(h)
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
            node.next = None
            cur.next = node
            cur = cur.next
            
        return head.next