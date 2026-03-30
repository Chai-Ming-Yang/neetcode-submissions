class Solution:
    def countBits(self, n: int) -> List[int]:
        """ look back """
        res = [0]
        for i in range(1, n+1):
            res.append(res[i // 2] + (1 & i))
        return res