# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = deque([root])
        res  = []
        while que:
            mx = float('-inf')
            for _ in range(len(que)):
                node  = que.popleft()
                mx  = max(mx , node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(mx)
        return res

