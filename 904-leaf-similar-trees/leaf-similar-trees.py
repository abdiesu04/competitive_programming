# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node , leafs):
            if not node.right and not node.left:
                leafs.append(node.val)
            
            if node.left:
                dfs(node.left , leafs)
            if node.right:
                dfs(node.right, leafs)
            return leafs
                
        
        return dfs(root1, []) == dfs(root2, [])