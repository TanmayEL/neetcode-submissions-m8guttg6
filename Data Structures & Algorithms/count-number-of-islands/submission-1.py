class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        q = deque()
        count = 0


        def bfs(i, j):
            q.append((i, j))
            seen.add((i, j))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                i, j = q.popleft()
                for dr, dc in directions:
                    nr = i + dr
                    nc = j + dc
                    
                    if((nr in range(ROWS)) and (nc in range(COLS)) and
                        (nr, nc) not in seen and
                        grid[nr][nc] == '1'):
                        q.append((nr, nc))
                        seen.add((nr, nc))
            

        for i in range(ROWS):
            for j in range(COLS):
                if ((i, j) not in seen and
                    grid[i][j] == '1'):
                    bfs(i, j)
                    count += 1
        return count