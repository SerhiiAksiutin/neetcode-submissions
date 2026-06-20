class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows = len(grid)
        cols = len(grid[0])    
        visited = set([(0, 0)])
        queue = deque([(0, 0)])
        

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    print(nr, nc)
                    if min(nr, nc) < 0 or nr == rows or nc == cols or (nr, nc) in visited or grid[nr][nc] == 1:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
            length += 1 
        
        return -1
