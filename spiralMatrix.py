class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # (row, col): 1 -> increase, -1 -> decrease
        r, l, t, b = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        n = len(matrix[0])
        m = len(matrix)

        res = []

        def isValid(i, j):
            if i >= m or i < 0:
                return False
            if j >= n or j < 0:
                return False
            if matrix[i][j] == '#':
                return False
            return True
        
        def nextTurn(turn):
            if turn == r:
                return b
            elif turn == b:
                return l
            elif turn == l:
                return t
            else:
                return r

        def isEnd(i, j):
            if isValid(i, j) and matrix[i][j] != '#':
                return False
            for turn in [r, l, t, b]:
                if isValid(i + turn[0], j + turn[1]):
                    return False
            return True

        row, col = 0, 0
        turn = r
        while not isEnd(row, col):
            while isValid(row, col):
                res.append(matrix[row][col])
                matrix[row][col] = '#'
                row = row + turn[0]
                col = col + turn[1]
            
            curRow, curCol = row - turn[0], col - turn[1]
            turn = nextTurn(turn)
            row, col = curRow + turn[0], curCol + turn[1]

        return res
