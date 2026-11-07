class Solution:
    def isBalanced(self, root) -> bool:

        # at each level we have to check if it is balanced or not
        #
        def dfs(curr):

            if not curr:
                return [True, 0]

            # check on both left and right subtree
            left, right = dfs(curr.left), dfs(curr.right)

            # for balanced condition it has to satisfy both conditions of being True in balance and also the height diff be <= 1
            balanced = (
                left[0] == True and right[0] == True and abs(left[1] - right[1]) <= 1
            )

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
