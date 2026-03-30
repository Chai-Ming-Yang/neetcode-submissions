class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minH = [-stone for stone in stones]
        heapq.heapify(minH)

        while len(minH) > 1:
            a, b = heapq.heappop(minH), heapq.heappop(minH)
            diff = -abs(a-b)
            if diff:
                heapq.heappush(minH, diff)
        return -minH[0] if minH else 0