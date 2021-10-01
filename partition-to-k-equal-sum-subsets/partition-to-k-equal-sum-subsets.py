class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_array_sum = sum(nums)
        n = len(nums)
        
        if total_array_sum % k != 0:
            return False
        
        target_sum = total_array_sum // k
        
        nums.sort(reverse=True)
        
        taken = [False] * n
        
        def backtrack(index, count: int, curr_sum: int) -> bool:
            n = len(nums)
            # We made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k-1:
                return True
            
            if curr_sum > target_sum:
                return False
            
            if curr_sum == target_sum:
                return backtrack(0, count + 1, 0)
            
            for j in range(index, n):
                if not taken[j]:
                    taken[j] = True
                    
                    if backtrack(j + 1, count, curr_sum + nums[j]):
                        return True
                    
                    taken[j] = False
        
        return backtrack(0, 0, 0)