class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for i in range(n)]
        cols = set()
        # (r - c) is same for all cells in downward diagonal (going left -> right)
        neg_diag = set() # e.g. (0,0), (1,1), (2,2)
        # (r + c) is same for all cells in upward diagonal (going left -> right)
        pos_diag = set() # e.g. (2,0), (1,1), (0,2)
        
        # adds queen row by row, starting at row r
        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            # check each column in row r to see if safe from previous queens
            for c in range(n):
                # if unsafe, backtrack
                if c in cols or (r - c) in neg_diag or (r + c) in pos_diag:
                    continue
                
                # if safe, add queen and explore next row
                cols.add(c)
                neg_diag.add(r - c)
                pos_diag.add(r + c)

                board[r][c] = 'Q'
                backtrack(r + 1)
                # backtrack, re-explore row r but for different column c
                board[r][c] = '.'

                cols.remove(c)
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)

        
        backtrack(0)
        return res
