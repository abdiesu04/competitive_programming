# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        queue = deque([(root,1)])

        while queue:
            current_width  = queue[-1][1] - queue[0][1] + 1
            max_width = max(max_width, current_width)

            for i in range(len(queue)):
                node , index = queue.popleft()

                if node.left:
                    queue.append((node.left , index * 2 ))
                if node.right:
                    queue.append((node.right , index * 2 +1 ))
                    
        return max_width