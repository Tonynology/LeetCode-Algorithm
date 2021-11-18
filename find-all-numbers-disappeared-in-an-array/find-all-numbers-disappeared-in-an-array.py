class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # using hash, O(n), O(n)
        hashTable = {}
        
        for num in nums:
            hashTable[num] = 1
            
        output = []
        for i in range(1, len(nums) + 1):
            if i not in hashTable:
                output.append(i)
        
        return output