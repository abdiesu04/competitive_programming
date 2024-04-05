class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        res = []
        
        queue.append(root)
        while queue:
            level_sum = 0
            level_count = len(queue)
            
            for i in range(level_count):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level_sum / level_count)
        
        return res