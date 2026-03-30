class Solution:
    def areFreqEqual(self, f1, f2, t):
        for c in t:
            if c not in f2 or f1[c] > f2[c]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        freq1 = {}
        freq2 = {}

        for c in t:
            freq1[c] = 1 + freq1.get(c, 0)

        ans = ''
        minlen = 1001
        l, r = 0, 0

        while r < len(s):
            while r < len(s) and not self.areFreqEqual(freq1, freq2, t):
                freq2[s[r]] = 1 + freq2.get(s[r], 0)
                r += 1
            while l <= r and self.areFreqEqual(freq1, freq2, t):
                curr_len = r - l
                if curr_len < minlen:
                    ans = s[l:r]
                    minlen = curr_len
                freq2[s[l]] -= 1
                l += 1
        return ans
            
