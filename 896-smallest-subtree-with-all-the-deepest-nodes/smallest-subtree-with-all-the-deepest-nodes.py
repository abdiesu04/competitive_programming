# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return (None , 0)

            left_lca , left_depth = dfs(node.left)
            right_lca , right_depth = dfs(node.right)

            if left_depth == right_depth:
                return (node , left_depth + 1)
            elif right_depth > left_depth:
                return (right_lca , right_depth + 1)
            else:
                return (left_lca ,left_depth + 1)

        return dfs(root)[0]