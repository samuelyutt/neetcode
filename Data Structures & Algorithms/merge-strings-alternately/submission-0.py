class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ret = ''
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                ret += word1[i]
            if i < len(word2):
                ret += word2[i]
            i += 1
        return ret