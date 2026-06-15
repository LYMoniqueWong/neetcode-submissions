class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for c, p in prerequisites:
            adjList[c].append(p) # 1: 0 take 0 be4 1
        
        res, visit = [], {} #visit True: in current path; False: fully processed
        # res 0 1
        def dfs(c): # detects cycle + handle ordering
            if c in visit:
                return visit[c]
            visit[c] = True
            for p in adjList[c]:
                if dfs(p):
                    return True
            res.append(c)
            visit[c] = False
            return False

        for i in range(numCourses):
            if dfs(i):
                return []
        
        return res