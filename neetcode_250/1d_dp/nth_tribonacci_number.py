class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        result = [-1] * (n + 1)
        result[0] = 0
        result[1] = 1
        result[2] = 1

        for i in range(3, n + 1):
            result[i] = result[i - 3] + result[i - 2] + result[i - 1]

        return result[n]
