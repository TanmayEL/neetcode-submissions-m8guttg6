class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        count = 0

        def bfs(r, c):
            q = deque()

            q.append((r, c))
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(ROWS) and 
                        c in range(COLS) and
                        grid[r][c] == '1' and
                        (r, c) not in visited):
                            q.append((r, c))
                            visited.add((r, c))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    count += 1
        
        return count
