class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = collections.defaultdict(set) # key = row num : int
        colSet = collections.defaultdict(set) # key = col num : int
        boxSet = collections.defaultdict(set) # key = box location : (int, int)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if (num != '.' and # ignore empty spots
                    (num in rowSet[r] or # number already in row
                    num in colSet[c] or # number already in col
                    num in boxSet[(r//3, c//3)]) # number already in box
                ):
                    return False
                
                rowSet[r].add(num)
                colSet[c].add(num)
                boxSet[(r//3,c//3)].add(num)
        
        return True
