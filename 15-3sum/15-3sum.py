class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSum(nums, i, res)

        return res

    def twoSum(self, nums, idx, res):
        low = idx + 1
        high = len(nums) - 1

        while low < high:
            Sum = nums[idx] + nums[low] + nums[high]
            if Sum > 0:
                high -= 1
            elif Sum < 0:
                low += 1
            else:
                res.append((nums[idx], nums[low], nums[high]))
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1