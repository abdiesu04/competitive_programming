"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        depth = 0
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node  = queue.popleft()

                for child in node.children:
                    queue.append(child)
            depth += 1
        return depth 