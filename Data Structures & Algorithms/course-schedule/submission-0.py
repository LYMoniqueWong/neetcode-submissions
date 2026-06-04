class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visitSet = set() # all course along curr dfs path
        def classOk(crs):
            if preMap[crs] == []:
                return True
            if crs in visitSet:
                return False
            visitSet.add(crs)
            for p in preMap[crs]:
                if not classOk(p): return False
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not classOk(crs): return False
        return True
