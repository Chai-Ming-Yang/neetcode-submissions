class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        q = deque([(i, 0, i) for i in range(N)])
        while q:
            for _ in range(len(q)):
                cur, curgas, ori = q.popleft()
                curgas += gas[cur] - cost[cur]
                if curgas < 0: continue
                if (cur - ori) % N == N-1: return ori
                q.append(((cur+1)%N, curgas, ori))
        return -1
