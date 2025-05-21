class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOARD_SIZE = 9
        BOX_SIZE = 3

        row_map = defaultdict(set)
        col_map = defaultdict(set)
        box_map = defaultdict(set)

        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                cell = board[r][c]
                if cell != '.':
                    if (cell not in row_map[r] and 
                        cell not in col_map[c] and
                        cell not in box_map[(r//BOX_SIZE, c//BOX_SIZE)]):
                        row_map[r].add(cell)
                        col_map[c].add(cell)
                        box_map[(r//BOX_SIZE, c//BOX_SIZE)].add(cell)
                    else:
                        return False
        
        return True
