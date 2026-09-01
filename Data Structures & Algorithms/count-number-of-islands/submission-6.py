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

            while queue:
                for i in range(len(queue)):
                    # print(len(queue))
                    row, col = queue.popleft()
                    # print(row, col)
                    # print()

                    

                    directoins = [
                        [-1,0], # Up
                        [1, 0], # Down
                        [0,-1], # Left
                        [0, 1]  # Right
                    ]

                    for row_direction, col_direction in directoins:
                        # print(row_direction, "|",col_direction)
                        # row, col = row + row_direction, col + col_direction
                        
                        if min(row + row_direction, col + col_direction) < 0 or \
                            row + row_direction >= len(grid) or \
                            col + col_direction >= len(grid[0]) or \
                            grid[row + row_direction][col + col_direction] == "0":
                            # print(row + row_direction, col + col_direction)
                            continue

                        queue.append((row + row_direction, col + col_direction))
                        grid[row + row_direction][col + col_direction] = "0"
                        

                       
            # print(grid)            
                    

        island = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    island += 1
                    bfs(row, col)
        # bfs(0, 0)
                    # dfs(row, col)
        return island