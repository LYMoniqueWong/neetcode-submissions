class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        heap = [-c for c in cnt.values()]
        heapq.heapify(heap)
        q = deque() # [-count left, available time]
        time = 0

        while heap or q:
            time += 1
            if heap:
                c = 1 + heapq.heappop(heap)
                if c:
                    q.append([c, time+n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time
        