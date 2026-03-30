class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        left, right = height[l], height[r]
        while l < r:
            if left < right:
                l += 1
                res += max(left - height[l], 0)
                left = max(left, height[l])
            else:
                r -= 1
                res += max(right - height[r], 0)
                right = max(right, height[r])
        return res