# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res  = 0

        node_stack = [(root , 1)]

        while node_stack:
            current_node , depth = node_stack.pop()
            res = max(res , depth)
            if current_node.left:
                node_stack.append((current_node.left , depth+1))
            if current_node.right:
                node_stack.append((current_node.right , depth+1))

        return res

            
