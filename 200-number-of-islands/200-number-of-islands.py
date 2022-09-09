class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        island = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # out of contidion
            # r is not in row range
            # c is not in col range
            # grid[r][c] == 0
            # grid[r][c] is in visited
            
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visited
            ):
                return
            
            visited.add((r, c))
            direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for dr, dc in direction:
                dfs(r + dr, c + dc)            
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    island += 1
                    dfs(row, col)
        
        return island