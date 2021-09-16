class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        direction = 0
        output = []
        
        while top <= down and left <= right:
            if direction == 0:
                for i in range(left, right+1):
                    output.append(matrix[top][i])
                top += 1
                
            elif direction == 1:
                for j in range(top, down+1):
                    output.append(matrix[j][right])
                right -= 1
                
            elif direction == 2:
                for k in reversed(range(left, right+1)):
                    output.append(matrix[down][k])
                down -= 1
                
            elif direction == 3:
                for p in reversed(range(top, down+1)):
                    output.append(matrix[p][left])
                left += 1
                
            
            direction = (direction + 1) % 4
            
        return output