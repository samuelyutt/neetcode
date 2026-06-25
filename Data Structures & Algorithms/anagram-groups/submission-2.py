class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            mark = [0] * 26
            for c in word:
                mark[ord(c) - ord('a')] += 1
            d[tuple(mark)].append(word)
        
        return list(d.values())