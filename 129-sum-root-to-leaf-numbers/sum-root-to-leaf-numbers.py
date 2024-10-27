# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res  = []
        def dfs(node , path):
            path += str(node.val)
            if not node.right and not node.left:
                res.append(int(path))
                return 
            
            if node.left:
                dfs(node.left , path)
            if node.right:
                dfs(node.right , path)

        dfs(root , '')
        print(res)
        return sum(res)