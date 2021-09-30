class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        return max(cnt.keys(), key=cnt.get)