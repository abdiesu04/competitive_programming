# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right , key)
        elif key < root.val:
            root.left = self.deleteNode(root.left , key)

        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            succossor = self.findMin(root.right)
            root.val = succossor.val
            root.right = self.deleteNode(root.right , succossor.val)
        return root

    def findMin(self , node):
        current = node
        while current.left:
            current = current.left
        return current
    
