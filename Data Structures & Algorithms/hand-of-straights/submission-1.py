class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = {}
        mn = []
        for h in hand:
            freq[h] = freq.get(h, 0) + 1
        mn = list(freq.keys())
        heapq.heapify(mn)

        while mn:
            first = mn[0]
            toPop = []
            for i in range(first, first + groupSize):
                if i not in freq: return False
                freq[i] -= 1
                if freq[i] == 0:
                    if mn[0] != i: return False
                    heapq.heappop(mn)

        return True