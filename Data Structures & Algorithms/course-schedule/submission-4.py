class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}

        for c1, c2 in prerequisites:
            adj[c1].append(c2)
        
        seen = set()

        def dfs(i):
            if adj[i] == []: return True

            if i in seen:
                return False

            seen.add(i)

            for preq in adj[i]:
                if not dfs(preq):
                    return False
            
            adj[i] = []
            seen.remove(i)
            return True
        
        for preq in prerequisites:
            if not dfs(preq[0]):
                return False
        
        return True

