class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        print(hand)
        N = len(hand)
        vis = [False] * N
        for l in range(N):
            if vis[l]: continue
            vis[l] = True
            r, times = l+1, 1
            pre = hand[l]
            while times < groupSize and r < N:
                if vis[r] or vis[r-1] and hand[r] == pre: r += 1; continue
                if hand[r] != times + hand[l]: return False
                vis[r] = True
                pre = hand[r]
                r += 1; times += 1
            if times != groupSize: return False
        return True