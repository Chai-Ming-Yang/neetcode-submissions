class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        look at prev (total_bit - 1) version
        if odd, + 1 bit
        """
        dp = [0] * (n + 1)
        for i in range(n+1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp