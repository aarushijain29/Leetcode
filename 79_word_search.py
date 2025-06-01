class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def is_valid_unvisited_cell(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and board[i][j] != '#'

        def backtrack(r, c, i):
            if i == len(word): return True
            if not is_valid_unvisited_cell(r, c) or board[r][c] != word[i]: return False

            board[r][c] = '#'
            res = (
                backtrack(r + 1, c, i + 1)
                or backtrack(r - 1, c, i + 1)
                or backtrack(r, c + 1, i + 1)
                or backtrack(r, c - 1, i + 1)
            )
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
            
            
        return False
