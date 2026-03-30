class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """ CONCEPT:
            - n parentheses (open & close)
            - string can only begin with open parenthesis
            -    ''   ''  ''  end with close parenthesis

            - track open & close count. (LEFT to RIGHT)     
                - close > open   invalid
                - close == open  (only '(' allowed)
                - close < open   (both '(',')' allowed)
            
            RULE: 
            1. '(' can be added if:
                - countOpen < n
            2. ')' can be added if:
                - countClose < countOpen
        """
        stack = [] 
        res = []

        def backtrack(openN, closedN):
            # base case
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0,0)
        return res

