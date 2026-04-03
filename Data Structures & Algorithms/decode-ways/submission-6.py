class Solution:
    def numDecodings(self, s: str) -> int:
        """ tabulation """
        if not s or s[0] == '0': return 0
        N = len(s)
        dp = [0] * N
        dp[0] = 1
        for i in range(1, N):
            if s[i] != '0':
                dp[i] = dp[i-1]
            if 9 < int(s[i-1: i+1]) <= 26:
                dp[i] += 1 if i < 2 else dp[i-2]
        return dp[-1]