class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        
        def dfs(i, j):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            seen.add((i, j))
            area = 1

            for dr, dc in directions:
                r, c = i + dr, j + dc

                if((r in range(ROWS)) and
                        c in range(COLS) and
                        (r, c) not in seen and
                        grid[r][c] == 1):
                        area += dfs(r, c)
            return area
                

        
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in seen and
                    grid[r][c] == 1):
                    max_area = max(max_area, dfs(r, c))
        
        return max_area