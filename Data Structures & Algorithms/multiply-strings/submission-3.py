class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = n2 = 0
        for c in num1:
            n1 *= 10
            n1 += (ord(c) - ord('0'))
        for c in num2:
            n2 *= 10
            n2 += (ord(c) - ord('0'))
        
        n1 *= n2
        n = ''
        while n1:
            n += chr(ord('0') + (n1%10))
            n1 //= 10

        return n[::-1] if n else '0'