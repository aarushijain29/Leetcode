class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def is_valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1'

        def dfs(r, c):
            if not is_valid(r, c):
                return
            
            grid[r][c] = '#'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def bfs(r, c):
            neighbours = deque()
            neighbours.append((r, c))

            while neighbours:
                row, col = neighbours.popleft()
                grid[row][col] = '#'
                for dr, dc in directions:
                    if is_valid(row + dr, col + dc):
                        neighbours.append((row + dr, col + dc))
                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r,c)
                    res += 1
        return res
