class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        left, right = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
        up, down = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
        m = set(tuple(mine) for mine in mines)
        
        for x in range(n):
            for y in range(n):
                if (x, y) in m:
                    left[x][y] = 0
                    up[x][y] = 0
                elif x == 0 or y == 0:
                    left[x][y] = 1
                    up[x][y] = 1
                else:
                    left[x][y] = left[x][y-1]+1
                    up[x][y] = up[x-1][y]+1
                
                nx, ny = n-x-1, n-y-1
                if (nx, ny) in m:
                    right[nx][ny] = 0
                    down[nx][ny] = 0
                elif nx == n-1 or ny == n-1:
                    right[nx][ny] = 1
                    down[nx][ny] = 1
                else:
                    right[nx][ny] = right[nx][ny+1]+1
                    down[nx][ny] = down[nx+1][ny]+1
                
        res = 0
        for i in range(n):
            for j in range(n):
                res = max(res, min(left[i][j], right[i][j], up[i][j], down[i][j]))
        return res