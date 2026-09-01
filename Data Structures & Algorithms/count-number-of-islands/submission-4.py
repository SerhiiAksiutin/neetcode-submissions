class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return

        def dfs(row, col):
            # Base case:
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row + 1, col) # Up
            dfs(row - 1, col) # Down
            dfs(row, col - 1) # Left
            dfs(row, col + 1) # Right

        island = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    island += 1
                    dfs(row, col)
        return island