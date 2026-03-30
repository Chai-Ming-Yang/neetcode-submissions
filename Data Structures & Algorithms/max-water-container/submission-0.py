class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1
        while l < r:
            left, right = heights[l], heights[r]
            res = max(res, min(left, right) * (r-l))
            if left < right:
                l += 1
            elif left > right:
                r -= 1
            else:
                l += 1
                r -= 1

        return res