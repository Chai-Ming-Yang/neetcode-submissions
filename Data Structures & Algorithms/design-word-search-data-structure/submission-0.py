class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.child: 
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        q = deque([self.root])
        for c in word:
            for _ in range(len(q)):
                cur = q.popleft()
                if c == '.':
                    for val in cur.child.values():
                        q.append(val)
                elif c in cur.child:
                    q.append(cur.child[c])
            if not q: return False
        
        for cur in q:
            if cur.isEnd:
                return True
        return False