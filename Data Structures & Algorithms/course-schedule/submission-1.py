class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for preq in prerequisites:
            preMap[preq[0]].append(preq[1])
        seen = set()

        def dfs(course):
            if course in seen:
                return False
            if preMap[course] == []:
                return True
            
            seen.add(course)

            for preq in preMap[course]:
                if not dfs(preq):
                    return False
            seen.remove(course)
            preMap[course] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True

            