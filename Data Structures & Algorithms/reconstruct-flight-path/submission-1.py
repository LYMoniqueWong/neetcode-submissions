class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for s, e in tickets:
            adj[s].append(e)
        for src in adj:
            adj[src].sort(reverse=True)
        stack, res = ["JFK"], []
        while stack:
            src = stack[-1]
            if adj[src]:
                stack.append(adj[src].pop())
            else:
                res.append(stack.pop())
        return res[::-1]