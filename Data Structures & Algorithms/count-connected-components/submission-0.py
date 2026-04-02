class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1

        adj = {i : [] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        seen = set()

        def dfs(node, prev):
            if node in seen:
                return 0
            
            seen.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue
                dfs(nei, node)
        
            return 1
        
        res = 0
        for i in range(n):
            res += dfs(i, -1)

        print(res)
        return res