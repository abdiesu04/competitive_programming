# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])
        parent = {}
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                    parent[node.right.val] = node.val
                if node.left:
                    queue.append(node.left)
                    parent[node.left.val] = node.val

                level.append(node.val)
            if x in level and y in level and parent[x] != parent[y]:
                                 return True
        return False
                                 
                