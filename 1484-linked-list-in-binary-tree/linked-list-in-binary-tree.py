# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def checkpath(node , temp):
            if not temp:
                return True

            if not node:
                return False

            if node.val == temp.val:
                return checkpath(node.left , temp.next) or checkpath(node.right , temp.next)
            return False

        def dfs(node):
            if not node:
                return False

            if node.val == head.val and checkpath(node , head):
                return True

            return dfs(node.right) or dfs(node.left)

        return dfs(root)



            