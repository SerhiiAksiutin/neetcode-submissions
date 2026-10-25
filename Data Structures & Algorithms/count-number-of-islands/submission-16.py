from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row, col):
            queue = deque()
            directions = [
                (-1,0), # Up
                (1, 0), # Down
                (0,-1), # Left
                (0, 1)  # Right
            ]

            queue.append((row, col))

            while queue:
                row, col = queue.popleft()
                for row_direct, col_direct in directions:
                    next_row, next_col = row + row_direct, col + col_direct
                    if min(next_row, next_col) < 0 or \
                       next_row >= len(grid) or \
                       next_col >= len(grid[0]) or \
                       grid[next_row][next_col] == "0":
                        continue
                    queue.append((next_row, next_col))
                    grid[next_row][next_col] = "0"
        
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    islands += 1
                    bfs(row, col)
                    # dfs(row, col)
        
        return islands