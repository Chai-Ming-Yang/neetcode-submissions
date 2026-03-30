class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in {'+', '-', '*', '/'}:
                stack.append(c)
                continue
            b = int(stack.pop())
            a = int(stack.pop())
            if c == '+':
                stack.append(a+b)
            elif c == '-':
                stack.append(a-b)
            elif c == '*':
                stack.append(a*b)
            elif c == '/':
                stack.append(a/b)
        return int(stack[-1])