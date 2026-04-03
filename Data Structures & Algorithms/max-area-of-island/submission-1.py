class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        
        def bfs(i, j):
            if (i, j) in seen: return 0

            q = deque()

            q.append([i, j])
            seen.add((i, j))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            count = 1

            while q:
                i, j = q.popleft()

                for dr, dc in directions:
                    r, c = i + dr, j + dc

                    if((r in range(ROWS)) and
                        c in range(COLS) and
                        (r, c) not in seen and
                        grid[r][c] == 1):

                        q.append([r, c])
                        seen.add((r, c))
                        count += 1
            
            return count


        
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area