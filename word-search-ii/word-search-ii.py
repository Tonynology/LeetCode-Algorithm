class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
    def insert(self, word: str) -> None:
        curr = self
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            
        curr.endOfWord = True
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for word in words:
            root.insert(word)
        print(root)
        rows = len(board)
        cols = len(board[0])
        output = set()
        visited = set()
        
        def dfs(row, col, node, word):
            if (row < 0 or col < 0 or row == rows or col == cols or (row, col) in visited or board[row][col] not in node.children):
                return
            
            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.endOfWord:
                output.add(word)
                
            dfs(row+1, col, node, word)
            dfs(row, col+1, node, word)
            dfs(row-1, col, node, word)
            dfs(row, col-1, node, word)        
                        
            visited.remove((row, col))
        
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")
                
        return list(output)
                