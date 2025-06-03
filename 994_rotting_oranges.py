class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_valid_fresh(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == FRESH

        q = deque()
        fresh_cnt = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
                if grid[r][c] == FRESH:
                    fresh_cnt += 1
        
        # time = 0 is when we have already processed rotten oranges 
        # which we havent done now as they are still in q so time = -1 
        # so that post processing the rotten oranges time = 0 which is when we start seeing fresh oranges rot
        time = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid_fresh(nr, nc):
                        fresh_cnt -= 1
                        grid[nr][nc] = ROTTEN
                        q.append((nr, nc))
            time += 1

        return max(time, 0) if fresh_cnt == 0 else -1
