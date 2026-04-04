class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        vis = [False] * (amount + 1)
        vis[0] = True
        q = deque([0])
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt > amount or vis[nxt]: continue
                    if nxt == amount: return res
                    vis[nxt] = True
                    q.append(nxt)
        return -1