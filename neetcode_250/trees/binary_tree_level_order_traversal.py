# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        wrap_list = []
        if not root:
            return wrap_list

        queue = deque()
        queue.append(root)

        while queue:
            level_nums = len(queue)
            sub_list = []
            for _ in range(level_nums):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                sub_list.append(node.val)
            wrap_list.append(sub_list)

        return wrap_list
