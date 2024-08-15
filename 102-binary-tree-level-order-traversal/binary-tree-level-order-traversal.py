# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 

        queue = deque()
        queue.append(root)
        res  = []
        while queue:

            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            res.append(temp)
        return res
                