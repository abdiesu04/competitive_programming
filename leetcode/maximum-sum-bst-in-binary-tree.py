# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        mxSum = 0  
        def dfs(node):
            nonlocal mxSum 
            if node is None:
                return True, float('inf'), float('-inf'), 0
            
            lBst, lmin, lmax, lsum = dfs(node.left)
            rBst, rmin, rmax, rsum = dfs(node.right)

            if lBst and rBst and lmax < node.val < rmin:  
                sbSum = lsum + rsum + node.val  
                mxSum = max(mxSum, sbSum)
                return True, min(lmin, node.val), max(rmax, node.val), sbSum
            else:
                return False, 0, 0, 0

        dfs(root) 
        return mxSum