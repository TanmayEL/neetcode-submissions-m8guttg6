class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for preq in prerequisites:
            preMap[preq[0]].append(preq[1])
        seen = set()
        cycle = set()
        ans = []
        def dfs(course):
            if course in cycle:
                return False
            if course in seen:
                return True
            
            cycle.add(course)

            for preq in preMap[course]:
                if not dfs(preq):
                    return False

            seen.add(course)
            cycle.remove(course)
            ans.append(course)
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): 
                return []
        
        return ans