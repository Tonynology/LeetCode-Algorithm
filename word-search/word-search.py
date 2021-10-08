class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        targetLen = len(word)
        
        def dfs(row, col, pos) -> bool:
            if targetLen == pos:
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[pos]:
                return False
            
            temp = board[row][col]
            
            board[row][col] = "#"
            
            res = dfs(row+1, col, pos+1) or dfs(row, col+1, pos+1) or dfs(row-1, col, pos+1) or dfs(row, col-1, pos+1)
            
            board[row][col] = temp
            
            return res
            
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
                
        return False
                
                        