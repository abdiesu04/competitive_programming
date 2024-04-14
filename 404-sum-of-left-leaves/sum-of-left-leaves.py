class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node):
            if not node:
                return

            if node.left and not node.left.left and not node.left.right:
                res.append(node.left.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return sum(res)