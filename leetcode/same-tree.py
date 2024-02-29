# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = True
        def postorder(p, q):
            nonlocal flag
            if p is None and q is None:
                return
            if (p and not q) or (not p and q):
                flag = False
                return
            if p.val != q.val:
                flag = False
            postorder(p.left, q.left)
            postorder(p.right, q.right)
            
        postorder(p, q)
        return flag

        