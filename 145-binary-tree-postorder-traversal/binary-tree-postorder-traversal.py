# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        node_stack = [root]

        while node_stack:
            current_node = node_stack.pop()
            res.append(current_node.val)
            if current_node.left:
                node_stack.append(current_node.left)
            if current_node.right:
                node_stack.append(current_node.right)

        res.reverse()
        return res

