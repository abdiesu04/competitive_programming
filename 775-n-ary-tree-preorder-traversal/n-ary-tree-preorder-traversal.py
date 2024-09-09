"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        node_stack = [root]

        while node_stack:
            current_node = node_stack.pop()
            res.append(current_node.val)
            for child in current_node.children[::-1]:
                node_stack.append(child)

        return res


