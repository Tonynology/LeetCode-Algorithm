# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        dq = collections.deque([(root, float('-inf'))])
        
        while dq:
            node, max_so_far = dq.popleft()
            if max_so_far <= node.val:
                res += 1
            if node.left:
                dq.append((node.left, max(node.val, max_so_far)))
            if node.right:
                dq.append((node.right, max(node.val, max_so_far)))
        
        return res