# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        node_stack= [root]
        new_node = TreeNode(val)
        if not root:
            return new_node
        current_node = root

        while node_stack:
            current_node = node_stack.pop()
            if current_node:
                if current_node.val < val:
                    if current_node.right:
                        node_stack.append(current_node.right)
                    else:
                        current_node.right = new_node
                elif current_node.val > val:
                    if current_node.left:
                        node_stack.append(current_node.left)
                    else:
                        current_node.left  = new_node

    
        return root

         