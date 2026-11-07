class Solution:
    def hammingWeight(self, n: int) -> int:
        # using kernighan's algorithm to calcualte the set bits
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
