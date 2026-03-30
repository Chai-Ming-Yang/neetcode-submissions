class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word: str):
        cur = self.root
        for c in word:
            cur.children[c] = cur.children.get(c, TrieNode())
            cur = cur.children[c]
        cur.isEnd = True
    def isPrefix(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:return False
            cur = cur.children[c]
        return True
    def isWord(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:return False
            cur = cur.children[c]
        return cur.isEnd

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefixTree = PrefixTree()
        for word in words:
            prefixTree.add(word)
        R, C = len(board), len(board[0])
        vis = set()
        visStr = []
        res = set()

        def dfs(r, c):
            if (r<0 or r==R or c<0 or c==C or
                (r,c) in vis or
                not prefixTree.isPrefix(''.join(visStr) + board[r][c])): 
                return
            vis.add((r,c))
            visStr.append(board[r][c])
            s = ''.join(visStr)
            if prefixTree.isWord(s) and s not in res: res.add(s)

            for newR, newC in {(r+1, c), (r-1, c), (r, c+1), (r, c-1)}:
                dfs(newR, newC)
            vis.remove((r,c))
            visStr.pop()


        for r in range(R):
            for c in range(C):
                dfs(r, c)

        return [a for a in res]