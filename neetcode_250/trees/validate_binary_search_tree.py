# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, -sys.maxsize - 1, sys.maxsize)

    def isValidBSTHelper(self, root, minVal, maxVal):
        if root == None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.isValidBSTHelper(
            root.left, minVal, root.val
        ) and self.isValidBSTHelper(root.right, root.val, maxVal)
