class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def dfs(i, j):
            if (i, j) in seen: return 0

            seen.add((i, j))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                r, c = i + dr, j + dc

                if (r in range(ROWS) and
                    c in range(COLS) and
                    (r, c) not in seen
                    and grid[r][c] == '1'):
                    dfs(r, c)
            return 1
        
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    count += dfs(i, j)
        
        return count
        