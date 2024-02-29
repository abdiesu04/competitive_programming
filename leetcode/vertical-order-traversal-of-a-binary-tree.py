# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        temp = []
        
        def dfs(root, row, col):
            if root:
                temp.append([row, col, root.val]) 
                dfs(root.left , row + 1 , col - 1)
                dfs(root.right , row + 1 , col + 1)  
        
        dfs(root, 0, 0)
        
        mapp = defaultdict(list)
        for row, col, val in temp:
            mapp[col].append((row, val))
        
        res = []

        mapp = dict(sorted(mapp.items()))
        print(mapp)

        for col in sorted(mapp.keys()):
            res.append([val for _, val in sorted(mapp[col])])

        return res