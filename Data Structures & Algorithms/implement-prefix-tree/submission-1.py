class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            key = ord(c) - ord('a')
            if not cur.child[key]: cur.child[key] = TrieNode()
            cur = cur.child[key]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            key = ord(c) - ord('a')
            if not cur.child[key]: return False
            cur = cur.child[key]
        return cur.isEnd
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            key = ord(c) - ord('a')
            if not cur.child[key]: return False
            cur = cur.child[key]
        return True