class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:  return True
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit, self.count = set(), 0
        
        def dfs(node, prevNode):
            if node in visit:
                return False
            visit.add(node)
            self.count += 1
            for nei in adj[node]:
                if nei == prevNode:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):  return False
        return self.count == n