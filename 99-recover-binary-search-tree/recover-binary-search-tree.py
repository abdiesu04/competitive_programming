# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            res.append(node)
            dfs(node.right)
        dfs(root)
        print(res)
        first , second = None , None
        for i in range(1, len(res)):
            if res[i].val < res[i - 1].val:
                # First violation: the first node out of order
                if not first:
                    first = res[i - 1]
                # Second violation: the second node out of order
                second = res[i]

        # Step 3: Swap the values of the two incorrect nodes
        if first and second:
            first.val, second.val = second.val, first.val