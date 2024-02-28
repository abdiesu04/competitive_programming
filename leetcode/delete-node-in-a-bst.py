class Solution:
    def findMin(self, root):
        node = root.right
        while node.left:
            node = node.left
        return node.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

            root.val = self.findMin(root)
            root.right = self.deleteNode(root.right, root.val)

        return root