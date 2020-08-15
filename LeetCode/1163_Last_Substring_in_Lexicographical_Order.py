class Solution:
    def lastSubstring(self, s: str) -> str:
        # Process 1
        mx = ""
        for i in range(len(s)):
            mx = max(mx, s[i:])
        return mx
        # Process 2
        c, n = max(s), len(s)
        if s == c*n:
            return s
        
        q = [i for i, e in enumerate(s) if e == c]
        res = s[q[0]]
        while q:
            qq = []
            for i in q:
                if i+1 < n:
                    qq += [i+1]
            if not qq:
                break
            c = max(s[i] for i in qq)
            res += c
            q = [i for i in qq if s[i] == c]
        
        return res
