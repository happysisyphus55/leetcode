# https://leetcode.com/problems/merge-strings-alternately/description/
class Solution:
    def mergeStringsAlternately(self, word1, word2):
        i = 0
        j = 0

        res = []

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])

            i += 1
            j += 1

        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)
