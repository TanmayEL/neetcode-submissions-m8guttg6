class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l, r = 0, 0
        len_s, len_t = len(s), len(t)

        while l < len_s and r < len_t:
            if l < len_s and s[l] == t[r]:
                l += 1
                r += 1
            else:
                l += 1
        
        return len_t - r
            