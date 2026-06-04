class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        memo = {}
        
        def search(i):
            if i >= len(s):
                return 0

            if i in memo:
                return memo[i]
            
            memo[i] = 1 + search(i + 1)

            for word in dictionary:
                if word == s[i:i + len(word)]:
                    memo[i] = min(memo[i], search(i + len(word)))
            
            return memo[i]

        return search(0)