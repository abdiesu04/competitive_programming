from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        queue = deque()
        results = []
        
        # Check if the root is None
        if root is None:
            return results
        
        queue.append(root)
        
        while len(queue) > 0:
            ql = len(queue)
            level = []
            
            for i in range(ql):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if level:
                results.append(level[-1])  # Append the last element of the level to results
        
        return results