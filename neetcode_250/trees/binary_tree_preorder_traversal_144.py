# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversals = []
        self._preorder_traversal(root, traversals)
        return traversals

    def _preorder_traversal(self, root, traversals):
        if not root:
            return

        traversals.append(root.val)
        self._preorder_traversal(root.left, traversals)
        self._preorder_traversal(root.right, traversals)
