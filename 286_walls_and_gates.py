class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        WALL = -1
        GATE = 0
        EMPTY = 2147483647
        ROWS, COLS = len(rooms), len(rooms[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and rooms[r][c] == EMPTY

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == GATE:
                    q.append((r, c))
        
        dist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc):
                        rooms[nr][nc] = dist
                        q.append((nr, nc))
            dist += 1
        
        return rooms
