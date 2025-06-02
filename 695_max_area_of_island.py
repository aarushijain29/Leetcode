class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def is_valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1

        def dfs(r, c):
            if is_valid(r, c):
                grid[r][c] = '#'
                return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            
            return 0

        for r in range(ROWS):
            for c in range(COLS):
                if is_valid(r, c):
                    res = max(res, dfs(r, c))

        return res
