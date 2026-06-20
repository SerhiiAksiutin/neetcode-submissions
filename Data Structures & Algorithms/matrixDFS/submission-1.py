class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        def backtrack(grid, r, c, visited):

            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 1 or (r, c) in visited:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            paths = 0
            visited.add((r, c))
            
            paths += backtrack(grid, r - 1, c, visited)
            paths += backtrack(grid, r, c - 1, visited)
            paths += backtrack(grid, r + 1, c, visited)
            paths += backtrack(grid, r, c + 1, visited)

            visited.remove((r, c))
            return paths
        
        return backtrack(grid, 0, 0, set())