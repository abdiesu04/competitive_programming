# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0
        def dfs(node , parent , grandparent):
            nonlocal result
            if not node:
                return 
            if grandparent and grandparent.val % 2 == 0:
                result += node.val

            dfs(node.left , node , parent)
            dfs(node.right , node , parent)
        dfs(root , None , None)
        return result
