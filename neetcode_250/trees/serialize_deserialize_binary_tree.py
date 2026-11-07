# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node is None:
                res.append("#")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        values = data.split(",")
        # create the root node from the first value
        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1

        while queue:
            node = queue.popleft()

            # proceed left child
            if values[index] != "#":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1

            # process right child
            if values[index] != "#":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
