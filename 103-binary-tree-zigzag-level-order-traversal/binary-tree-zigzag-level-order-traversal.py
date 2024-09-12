# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        queue = deque([root])
        result = []
        is_reverse = False

        while queue:
            temp = deque()
            for i in range(len(queue)):
                node = queue.popleft()
                if is_reverse:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(temp)
            result.append(temp)
            is_reverse = not is_reverse
        return result


