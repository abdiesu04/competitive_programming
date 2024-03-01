class Solution:
    def invertTree(self, root):
        # if not root:
        #     return None
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
            
            if node:
                queue.append(node.left)
                queue.append(node.right)
        
        return root