## given two trees -> check if both of them are same or not


class Solution:
    def isSameTree(self, p, q):

        # 1. base case when both trees are null
        if not p and not q:
            return True

        # 2. Base case when either of  the trees is null or the value doesnt match
        if not p or not q and (p.val != q.val):
            return False

        # 3. recursive case
        result = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return result
