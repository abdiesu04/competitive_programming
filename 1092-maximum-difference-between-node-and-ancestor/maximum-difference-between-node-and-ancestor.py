# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return float('inf') , float('-inf')
            
            if not node.left and not node.right:
                return node.val , node.val

            left_min , left_max = dfs(node.left)
            right_min , right_max = dfs(node.right)

            subtree_min = min(left_min , right_min)
            subtree_max = max(left_max , right_max)

            self.max_diff  = max(self.max_diff , abs(node.val - subtree_min) , abs(subtree_max - node.val))

            return min(subtree_min , node.val) , max(subtree_max , node.val)

        self.max_diff = 0

        dfs(root)
        return self.max_diff
            