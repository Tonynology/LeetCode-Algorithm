# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = curr_sum = 0
        h = defaultdict(int)
        
        def preorder(node, curr_sum):
            nonlocal count
            if not node:
                return None
            
            curr_sum += node.val
            
            if curr_sum == targetSum:
                count += 1
            
            count += h[curr_sum - targetSum]
            
            h[curr_sum] += 1
            
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            
            h[curr_sum] -= 1            
                 
        preorder(root, 0)
        return count