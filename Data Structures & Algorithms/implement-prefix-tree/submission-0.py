class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child: 
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.isEnd = True
        return

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not cur.child.get(c, False): return False
            cur = cur.child[c]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not cur.child.get(c, False): return False        
            cur = cur.child[c]
        return True