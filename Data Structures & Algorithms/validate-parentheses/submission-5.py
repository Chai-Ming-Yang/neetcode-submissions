class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        check = {'{':'}', '(':')', '[':']'}
        for c in s:
            if c in check:
                st.append(c);   continue
            if st and check[st[-1]] == c:
                st.pop();   continue
            return False
        return not st