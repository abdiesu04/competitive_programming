class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []

        def dfs(root):
            if not root:
                return
            if low <= root.val <= high:
                res.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        return sum(res)