class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N, l, r = len(s), 0, 0
        count = defaultdict(int)
        maxx = 0
        cmax = s[0]
        res = 0
        while r < N:
            count[s[r]] += 1
            if count[s[r]] > maxx:
                maxx = count[s[r]]
                cmax = s[r]
            maxx = max(maxx, count[s[r]])
            res = max(res, min(maxx + k, N))
            # print('r:', r)
            # print(cmax, maxx)
            # print(count)
            r += 1
            if maxx + k >= r-l:
                continue
            
            count[s[l]] -= 1
            l += 1
            if s[l] == cmax:
                maxx = 0
                for c, n in count.items():
                    if n > maxx:
                        maxx = n
                        cmax = c
        print(count.items(), maxx)
        print(res)
        return res