# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        
        if not root:
            return []
        
        queue.append(root)
        while queue:
            level = []
            level_count = len(queue)
            
            for i in range(level_count):
                node = queue.popleft()
                if node:
                    level.append( node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level)
        
        return res[::-1]