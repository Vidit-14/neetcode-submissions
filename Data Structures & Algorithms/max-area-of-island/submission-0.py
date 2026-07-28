class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxArea = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal maxArea

            stack = []
            stack.append((r, c))
            grid[r][c] = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            currArea = 1
            maxArea = max(currArea, maxArea)

            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        currArea += 1
                        maxArea = max(currArea, maxArea)
                        grid[r][c] = 0
                        stack.append((r, c))
                


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
        
        return maxArea