# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathDown(self, node, maxValue):
        if node == None:
            return 0

        left = max(0, self.maxPathDown(node.left, maxValue))
        right = max(0, self.maxPathDown(node.right, maxValue))

        maxValue[0] = max(maxValue[0], left + right + node.val)
        return max(left, right) + node.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxValue = [0]
        maxValue[0] = float("-inf")
        self.maxPathDown(root, maxValue)
        return maxValue[0]
