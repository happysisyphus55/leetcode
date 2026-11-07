# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversals = []
        self._postorder_traversal(root, traversals)
        return traversals

    def _postorder_traversal(self, root, traversals):
        if not root:
            return

        self._postorder_traversal(root.left, traversals)
        self._postorder_traversal(root.right, traversals)
        traversals.append(root.val)
