class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        maxheap = [-c for c in cnt.values()]
        heapq.heapify(maxheap)
        time, q = 0, deque()
        while maxheap or q:
            time += 1
            if maxheap:
                c = 1 + heapq.heappop(maxheap)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                    heapq.heappush(maxheap, q.popleft()[0])
        return time