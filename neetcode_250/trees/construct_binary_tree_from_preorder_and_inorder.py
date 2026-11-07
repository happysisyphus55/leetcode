# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        for i in range(0, len(inorder)):
            inMap[inorder[i]] = i

        root = self.buildTreeRec(
            preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inMap
        )
        return root

    def buildTreeRec(self, preOrder, preStart, preEnd, inOrder, inStart, inEnd, inMap):
        if preStart > preEnd or inStart > inEnd:
            return None

        root = TreeNode(preOrder[preStart])
        inRoot = inMap.get(root.val, 0)
        numsLeft = inRoot - inStart

        root.left = self.buildTreeRec(
            preOrder,
            preStart + 1,
            preStart + numsLeft,
            inOrder,
            inStart,
            inRoot - 1,
            inMap,
        )
        root.right = self.buildTreeRec(
            preOrder, preStart + numsLeft + 1, preEnd, inOrder, inRoot + 1, inEnd, inMap
        )
        return root
