class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited, prev):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                (r, c) in visited or
                heights[r][c] < prev):
                return
            
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])


        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        ans = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in atl:
                    ans.append([i, j])
        
        return ans