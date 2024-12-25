# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #     que = deque([root])
    #     res  = []
    #     while que:
    #         mx = float('-inf')
    #         for _ in range(len(que)):
    #             node  = que.popleft()
    #             mx  = max(mx , node.val)
    #             if node.left:
    #                 que.append(node.left)
    #             if node.right:
    #                 que.append(node.right)
    #         res.append(mx)
    #     return res
        mapp = {}
        def dfs(node , level):
            if not node:
                return 
            if level not in mapp:
                mapp[level] = float('-inf')
            mapp[level] = max(mapp[level] , node.val)

            if node.right:
                dfs(node.right , level + 1)
            if node.left:
                dfs(node.left , level + 1)

        dfs(root , 0)
        res = []
        for _ , val in mapp.items():
            res.append(val)
        return res
            

