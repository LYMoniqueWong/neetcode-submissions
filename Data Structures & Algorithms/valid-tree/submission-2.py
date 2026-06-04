class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:  return True
        if len(edges) != n-1:   return False
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
        dfs(0)
        return len(visit) == n
       