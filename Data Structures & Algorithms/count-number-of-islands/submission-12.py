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
                r, c = queue.popleft()
                for direction_r, direction_c in directions:
                    next_r, next_c = r + direction_r, c + direction_c
                    if min(next_r, next_c) < 0 or \
                       next_r >= len(grid) or \
                       next_c >= len(grid[0]) or \
                       grid[next_r][next_c] == "0":
                        continue
                    queue.append((next_r, next_c))
                    grid[next_r][next_c] = "0"
        
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    islands += 1
                    bfs(row, col)
        
        return islands