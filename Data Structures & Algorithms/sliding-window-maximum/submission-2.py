class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i, n in enumerate(nums[:k]):
            heapq.heappush(heap, (-n, i))
        
        res = [-heap[0][0]]
        l = 1
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            while heap[0][1] < l:
                heapq.heappop(heap)
            res += [-heap[0][0]]
            l += 1
        return res