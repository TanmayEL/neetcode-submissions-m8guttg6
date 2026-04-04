class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { i : [] for i in range(numCourses)}

        for preq in prerequisites:
            adj[preq[0]].append(preq[1])
        
        visiting, visited = set(), set()
        ans = []

        def dfs(i):
            if i in visiting:
                return False
            
            if i in visited:
                return True
            
            visiting.add(i)

            for nei in adj[i]:
                if not dfs(nei):
                    return False
                
            visited.add(i)
            ans.append(i)
            visiting.remove(i)
            return True



        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return ans
            