# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while True:
            # if both nodes are smalller than current node, LCA must be in left subtree
            if root.val < min(p.val, q.val):
                root = root.right
            # if both nodes are greater than current node, LCA must be in the right subtree
            elif root.val > max(p.val, q.val):
                root = root.left
            # current node is the LCA as
            # - one node is on the left and other is on the right of current node
            # - current node equals one of the target nodes
            else:
                return root
