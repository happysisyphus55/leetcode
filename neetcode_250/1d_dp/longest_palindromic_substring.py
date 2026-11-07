class Solution:
    def manacher(self, s):
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        l, r = 0, 0
        for i in range(n):
            p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
            while (
                i + p[i] + 1 < n
                and i - p[i] - 1 >= 0
                and t[i + p[i] + 1] == t[i - p[i] - 1]
            ):
                p[i] += 1
            if i + p[i] > r:
                l, r = i - p[i], i + p[i]
        return p

    def longestPalindrome(self, s: str) -> str:
        # pallindromic substring -> any substring written in reverse order is the same

        # brute force -> check every single substring and check if its a pallindrome

        # for a string -> check a a pallindrome (for a substring , o(n) tc.) -> substrings that we have to check (o(n)^2) -> o(n^3)

        #

        # res = ""
        # resLen = 0

        # for i in range(len(s)):
        #     # odd length
        #     l, r = i, i
        #     # check also if left and right equal and move outwards
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         #odd length
        #         if (r-l + 1) > resLen:
        #             # update result
        #             res = s[l:r+1]
        #             # update result length
        #             resLen = r - l + 1

        #     # even length
        #     l ,r = i , i +1
        #     #pallindrome condition
        #     while l >=0 and r < len(s) and s[l] == s[r]:
        #         if (r - l + 1) > resLen:
        #             res = s[l:r+1]
        #             resLen = r - l + 1
        #         l -= 1
        #         r += 1

        # return res
        # manacher's algorithm

        p = self.manacher(s)
        resLen, center_idx = max((v, i) for i, v in enumerate(p))
        resIdx = (center_idx - resLen) // 2
        return s[resIdx : resIdx + resLen]
