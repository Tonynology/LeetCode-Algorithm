class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hashmap:
                return [i, hashmap[remainder]]
            hashmap[nums[i]] = i