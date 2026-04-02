class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = {i : [] for i in range(n)}
        seen = set()

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(node, prev):
            if node in seen:
                return False
            
            seen.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        
        return dfs(0, -1) and len(seen) == n
                