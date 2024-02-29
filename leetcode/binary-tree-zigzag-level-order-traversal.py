class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        res = []
        queue.append(root)
        zigzag = True
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level and zigzag:
                res.append(level)
            elif level and not zigzag:
                res.append(level[::-1])
            zigzag = not zigzag
        return res