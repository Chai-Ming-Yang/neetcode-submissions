class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = [[-x, i] for i, x in enumerate(nums[:k-1])]
        heapq.heapify(h)
        res = []

        for i in range(k-1, len(nums)) :
            heapq.heappush(h, [-nums[i], i])
            print(i, h)
            while h[0][1] < (i - k + 1):
                heapq.heappop(h)
            res.append(-h[0][0])
        return res