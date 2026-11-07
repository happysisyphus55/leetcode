# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # subtree is valid if subRoot is null, and root being non null
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, q1, q2):
        if not q1 and not q2:
            return True

        if q1 and q2 and q1.val == q2.val:
            return self.sameTree(q1.left, q2.left) and self.sameTree(q1.right, q2.right)

        return False
