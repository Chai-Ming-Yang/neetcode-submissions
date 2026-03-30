class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        minH = [-v for v in freq.values()]
        heapq.heapify(minH) # maxHeap
        
        q = deque([])
        time = 0
        while minH or q:
            if minH:
                taskCount = heapq.heappop(minH)
                taskCount += 1  # reduce one
                if taskCount != 0:
                    q.append((time + n, taskCount))

            if q and q[0][0] == time:
                heapq.heappush(minH, q.popleft()[1])
            time += 1
        return time