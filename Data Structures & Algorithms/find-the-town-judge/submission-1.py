class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = set([i + 1 for i in range(n)])
        votes = {}
        for t in trust:
            candidates.discard(t[0])
            votes[t[1]] = votes.get(t[1], 0) + 1
        if len(candidates) == 1:
            candidate = candidates.pop()
            if votes[candidate] == n - 1:
                return candidate
        return -1