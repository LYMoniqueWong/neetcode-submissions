class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for c, p in prerequisites:
            adjList[c].append(p)
        visit = set()

        def dfs(i):
            if i in visit:
                return False
            if adjList[i] == []:
                return True
            visit.add(i)
            for p in adjList[i]:
                if not dfs(p):
                    return False
            visit.remove(i)
            adjList[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True