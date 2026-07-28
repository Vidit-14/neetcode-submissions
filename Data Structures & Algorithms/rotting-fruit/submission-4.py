class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        def addToQueue(r, c):
            nonlocal fresh
            
            if (r in range(rows) and c in range(cols) and grid[r][c] == 1):
                grid[r][c] = 2
                q.append((r, c))
                fresh -= 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        minute = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                addToQueue(r + 1, c)
                addToQueue(r - 1, c)
                addToQueue(r, c + 1)
                addToQueue(r, c - 1)

            minute += 1
        
        return minute if fresh == 0 else -1