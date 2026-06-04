class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit, coms = set(), 0
        def dfs(node): # marks visit
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)

        for i in range(n):
            if i in visit:
                continue
            dfs(i)
            coms += 1
        return coms