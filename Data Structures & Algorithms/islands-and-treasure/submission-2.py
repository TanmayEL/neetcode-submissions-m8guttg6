class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2** 31 - 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        level = 1 #dont cheap out on using constant space, you were stuck because you were assigning i + 1 you dumb fuck
        while q:
            level_len = len(q)
            for i in range(level_len):
                a, b = q.popleft()

                for dr, dc in directions:
                    r, c = a + dr, b + dc

                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == INF):

                        grid[r][c] = level
                        q.append((r, c))
            level += 1
        
        


