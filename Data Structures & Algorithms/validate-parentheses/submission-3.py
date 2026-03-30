class Solution:
    def isValid(self, s: str) -> bool:
        """ CHECKs:
            1. stack not empty          (when encounter closing)
            2. stack empty after done
            3. hash matchPairs

            # CLOSING matches most _recent_ opening
        """  

        stack = []
        check = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c in {'{', '[', '('}:
                stack.append(c)
                continue
            if not stack:
                return False
            if stack[-1]==check[c]:
                stack.pop()
            else:
                return False
        return True if not stack else False