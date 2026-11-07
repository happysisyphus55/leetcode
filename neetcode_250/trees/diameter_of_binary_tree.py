class Solution:
    def diameter(self, root):

        # using a dfs based apporach to traverse the tree and get the height and add 1 to it
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0

            left = curr.left
            right = curr.right

            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res
