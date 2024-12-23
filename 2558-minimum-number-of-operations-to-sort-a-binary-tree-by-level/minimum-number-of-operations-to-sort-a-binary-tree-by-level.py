# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def countMinOp(arr):
            swaps = 0
            target = sorted(arr)

            pos = {val: idx for idx, val in enumerate(arr)}

            for i in range(len(arr)):
                if arr[i] != target[i]:
                    swaps += 1

                    cur_pos = pos[target[i]]
                    pos[arr[i]] = cur_pos
                    arr[cur_pos] = arr[i]

            return swaps

        que  = deque([root])
        cnt = 0
        while que:
            level = []
            for _ in range(len(que)):
                node = que.popleft()
                level.append(node.val)

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)
            cnt += countMinOp(level)
                

        return cnt