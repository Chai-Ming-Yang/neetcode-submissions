class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbors = {}
        def mapWords(word):
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                neighbors[pattern] = neighbors.get(pattern, []) + [word]
        mapWords(beginWord)
        for word in wordList:
            mapWords(word)
        
        q = deque([beginWord])
        vis = set([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' +  word[j+1:]
                    for neiWord in neighbors[pattern]:
                        if neiWord not in vis:
                            vis.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0