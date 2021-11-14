class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n = len(characters)
        k = combinationLength
        
        def backtrack(first = 0, curr = []):
            if len(curr) == k:
                self.combinations.append(''.join(curr))
                return
            
            for i in range(first, n):
                curr.append(characters[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack()
        self.combinations.reverse()

    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# abcd, 3