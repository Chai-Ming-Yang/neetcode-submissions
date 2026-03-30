class Solution:
    def checkValidString(self, s: str) -> bool:
        l, w = [], []
        for i in range(len(s)):
            if   s[i] == '*': w.append(i)
            elif s[i] == '(': l.append(i)
            elif l: l.pop()
            elif w: w.pop()
            else: return False
        
        while l:
            if not w or w[-1] < l[-1]: return False
            w.pop()
            l.pop()
        return True