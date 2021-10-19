# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parentX = parentY = 0
        levelX = levelY = 0
        
        def dfs(node, parent, level):
            nonlocal parentX, parentY, levelX, levelY
            
            if not node:
                return None            
            if node.val == x:
                parentX = parent
                levelX = level
                print(parentX, levelX)
            if node.val == y:
                parentY = parent
                levelY = level
                print(parentY, levelY)            
            dfs(node.left, node.val, level + 1)
            dfs(node.right, node.val, level + 1)            
            
        dfs(root, root.val, 0)
        # print(parentX == parentY)
        # print(levelX == levelY)
        # print(parentX == parentY and levelX == levelY)
        return (parentX != parentY and levelX == levelY)