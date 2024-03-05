# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mapp = defaultdict(int)
        def dfs(node):
            if not node:
                return 
            mapp[node.val] += 1
            dfs(node.right)
            dfs(node.left)
        dfs(root)
        print(mapp)
        modes = []
        max_freq= 0
        for i in mapp.values():
            max_freq = max(max_freq, i)
            
        for key, value in mapp.items():
            if value == max_freq:
                modes.append(key)
        
        return modes