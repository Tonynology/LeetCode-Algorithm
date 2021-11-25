class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Divide & Conquer solution. O(n log(n)), O()
        def findBestSubarray(nums, left, right):
            if left > right:
                return float('-inf')
            
            mid = left + (right - left) // 2
            curr = best_left_sum = best_right_sum = 0
            
            for i in range(mid-1, left-1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)
                
            curr = 0
            for j in range(mid+1, right+1):
                curr += nums[j]
                best_right_sum = max(best_right_sum, curr)
                
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum
            
            left_half = findBestSubarray(nums, left, mid-1)
            right_half = findBestSubarray(nums, mid+1, right)
            
            return max(best_combined_sum, left_half, right_half)
        
        return findBestSubarray(nums, 0, len(nums)-1)
        
        
        # dp solution. O(n), O(1)
#         [-2,1,-3,4,-1,2,1,-5,4]
#         [-2,1,-2,4, 3,5,6, 1,5] and then find Max value of list.