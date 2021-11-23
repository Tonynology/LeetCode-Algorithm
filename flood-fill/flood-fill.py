class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old = image[sr][sc]
        if old != newColor:
            rows = len(image)
            cols = len(image[0])
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            Q = []
            Q.append((sr, sc))
            while Q:
                curr_x, curr_y = Q.pop(0)
                image[curr_x][curr_y] = newColor
                for i in range(4):
                    new_x = curr_x + dx[i]
                    new_y = curr_y + dy[i]
                    if new_x < 0 or new_y < 0 or new_x >= rows or new_y >= cols:
                        continue
                    if image[new_x][new_y] != old:
                        continue
                    Q.append((new_x, new_y))

        return image