class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        d = defaultdict(set) # wo*d -> set(word)
        e = defaultdict(list) # word -> [wo*d]
        for word in wordList + [beginWord, endWord]:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                d[key].add(word)
                e[word].append(key)

        traversed = set()
        q = deque([(beginWord, 1)])
        while q:
            word, num = q.popleft()
            if word == endWord:
                return num
            if word in traversed:
                continue
            traversed.add(word)
            for key in e[word]:
                for next_word in d[key]:
                    q.append((next_word, num + 1))
        return 0