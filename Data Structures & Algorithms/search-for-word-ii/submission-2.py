class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word: str):
        cur = self
        for c in word:
            cur.children[c] = cur.children.get(c, TrieNode())
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        R, C = len(board), len(board[0])
        vis, res = set(), set()
        
        def dfs(r, c, cur, word):
            if (r<0 or c<0 or r==R or c==C or
                (r,c) in vis or
                board[r][c] not in cur.children):
                return
            vis.add((r,c))
            cur = cur.children[board[r][c]]
            word += board[r][c]
            if cur.isWord: res.add(word)

            for newR, newC in {(r+1, c), (r-1, c), (r,c+1), (r,c-1)}:
                dfs(newR, newC, cur, word)
            vis.remove((r,c))
        
        for r in range(R): 
            for c in range(C):
                dfs(r, c, root, '')
        # return [word for word in res]
        return list(res)