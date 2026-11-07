class Solution:
    def isAnagram(self, s, t):
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if sorted_s == sorted_t:
            return True
        return False
