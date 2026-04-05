class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        directions = [[1, 0], [-1, 0 ], [0, 1], [0, -1]]

        def dfs(i, j):
            if board[i][j] == 'X':
                return
            if (i, j) in seen:
                return
            
            seen.add((i, j))

            for dr, dc in directions:
                r, c = i + dr, j + dc

                if (r in range(ROWS) and
                    c in range(COLS) and
                    (r, c) not in seen and
                    board[r][c] == 'O'):
                    dfs(r, c)


        for rows in range(ROWS):
            dfs(rows, 0)
            dfs(rows, COLS - 1)
        
        for cols in range(COLS):
            dfs(0, cols)
            dfs(ROWS - 1, cols)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i, j) not in seen:
                    board[i][j] = 'X'
