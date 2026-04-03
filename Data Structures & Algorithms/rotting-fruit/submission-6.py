class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        count = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    count += 1
        
        minute = 0
        while q and count > 0:
            for i in range(len(q)):
                a, b = q.popleft()

                for dr, dc in directions:
                    r, c = a + dr, b + dc

                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1):

                        q.append((r, c))
                        count -= 1
                        grid[r][c] = 2
            minute += 1
        
        return minute if count == 0 else -1
                