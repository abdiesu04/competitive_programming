# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0

        def dfs(node):
            nonlocal moves
            if not node:
                return 0
            left_moves = dfs(node.left)
            right_moves = dfs(node.right)
            moves += abs(left_moves) + abs(right_moves)
            return node.val + left_moves + right_moves - 1

        dfs(root)
        return moves