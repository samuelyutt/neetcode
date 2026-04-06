class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = strs[0]
        for i in range(1, len(strs)):
            ret = ret[:min(len(ret), len(strs[i]))]
            for j in range(len(ret)):
                if ret[j] != strs[i][j]:
                    ret = ret[:j]
                    break
        return ret