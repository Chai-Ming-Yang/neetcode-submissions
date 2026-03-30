class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}#{s}'
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1

            i += 1
            length = int(num)
            st = ''
            for _ in range(length):
                st += s[i]
                i += 1
            res.append(st)
        return res