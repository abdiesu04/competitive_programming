# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        
        def dfs(node, mn, mx):
            nonlocal ans
            if not node:
                return
            mn = min(mn, node.val)
            mx = max(mx, node.val)
            ans = max(ans, abs(node.val - mn), abs(node.val - mx))
            dfs(node.right, mn, mx)
            dfs(node.left, mn, mx)
        
        dfs(root, root.val, root.val)
        return ans