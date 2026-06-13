class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            cnts = [0] * 26
            for c in s:
                cnts[ord(c) - ord('a')] += 1

            for i in range(len(cnts)):
                cnts[i] = str(cnts[i])
            key = ' '.join(cnts)
            
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)

        ret = []
        for key, val in d.items():
            ret.append(val)
        return ret