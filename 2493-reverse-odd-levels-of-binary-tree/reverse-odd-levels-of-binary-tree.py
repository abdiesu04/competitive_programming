# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(level, left_node, right_node):
            if not left_node or not right_node:
                return
            
            if level % 2 == 1:
                left_node.val, right_node.val = right_node.val, left_node.val
            
            dfs(level + 1, left_node.left, right_node.right)
            dfs(level + 1, left_node.right, right_node.left)
        
        if root:
            dfs(1, root.left, root.right)
        return root
