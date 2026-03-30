class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        res = 0
        while l < r:
            left, right = height[l], height[r]
            if left < right:
                if left < lmax:
                    res += lmax - left
                else: 
                    lmax = left
                l += 1
            else:
                if right < rmax:
                    res += rmax - right
                else:
                    rmax = right
                r -= 1
        return res