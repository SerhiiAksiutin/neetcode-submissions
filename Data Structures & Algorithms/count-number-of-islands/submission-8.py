from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return

        # def dfs(row, col):
        #     # Base case:
        #     if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
        #         return

        #     grid[row][col] = "0"

        #     dfs(row + 1, col) # Up
        #     dfs(row - 1, col) # Down
        #     dfs(row, col - 1) # Left
        #     dfs(row, col + 1) # Right

        def bfs(row, col):
            
            queue = deque()
            queue.append((row, col))
            directoins = [
                [-1,0], # Up
                [1, 0], # Down
                [0,-1], # Left
                [0, 1]  # Right
            ]

            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()

                    for row_direction, col_direction in directoins:
                        
                        if min(row + row_direction, col + col_direction) < 0 or \
                            row + row_direction >= len(grid) or \
                            col + col_direction >= len(grid[0]) or \
                            grid[row + row_direction][col + col_direction] == "0":
                            continue

                        queue.append((row + row_direction, col + col_direction))
                        grid[row + row_direction][col + col_direction] = "0"        

        island = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    island += 1
                    bfs(row, col)
                    # dfs(row, col)
        return island