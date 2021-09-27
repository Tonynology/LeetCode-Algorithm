class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        
        offset = 1 if player == 1 else -1
        checkVal = self.size * offset
        
        self.rows[row] += offset
        self.cols[col] += offset
        
        if row == col:
            self.diagonal += offset
        
        if row + col == self.size - 1:
            self.anti_diagonal += offset
            
        if checkVal in [self.rows[row], self.cols[col], self.diagonal, self.anti_diagonal]:
            return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)