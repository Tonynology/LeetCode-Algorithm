class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        N = 3
        rows = [0] * N
        cols = [0] * N
        diagonal = anti_diagonal = 0
        
        player = 1
        for r, c in moves:
            rows[r] += player
            cols[c] += player
            if r == c:
                diagonal += player
            if r + c == N-1:
                anti_diagonal += player
                
            if abs(rows[r]) == N or abs(cols[c]) == N or abs(diagonal) == N or abs(anti_diagonal) == N:
                return "A" if player == 1 else "B"
            
            player = -player
            
        return "Draw" if len(moves) == N * N else "Pending"