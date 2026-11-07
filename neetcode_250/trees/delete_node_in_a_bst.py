# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delHelper(self, root):
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            rightChild = root.right
            lastRight = self.findLastRight(root.left)
            lastRight.right = rightChild
            return root.left

    def findLastRight(self, root):
        if root.right == None:
            return root
        return self.findLastRight(root.right)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return root

        if root.val == key:
            return self.delHelper(root)

        dummy = root
        while root != None:
            if root.val > key:
                if root.left != None and root.left.val == key:
                    root.left = self.delHelper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right != None and root.right.val == key:
                    root.right = self.delHelper(root.right)
                    break
                else:
                    root = root.right

        return dummy
