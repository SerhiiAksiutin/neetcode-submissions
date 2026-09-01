class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visit = set()

        
        def dfs(grid, r, c, visit):
            # Base case
            ROWS, COLS = len(grid), len(grid[0])
            if min(r, c) < 0 or \
            r >= ROWS or \
            c >= COLS or \
            (r, c) in visit or \
            grid[r][c] == "0":
                return
                

            visit.add((r, c))

            # Reccursion
            
            dfs(grid, r + 1, c, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r, c - 1, visit)

            return 1

            # visit.remove((r, c))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # if dfs(grid, i, j, visit):
                if grid[i][j] == '1' and (i, j) not in visit:
                    count += 1
                    dfs(grid, i, j, visit)
        
        return count