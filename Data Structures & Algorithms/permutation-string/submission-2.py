from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26

        for s in s1:
            freq1[ord(s) - ord('a')] += 1
        
        l, r = 0, 0
        while r < len(s1):
            freq2[ord(s2[r]) - ord('a')] += 1
            r += 1

        while r < len(s2):
            if freq1 == freq2:
                return True
            freq2[ord(s2[l]) - ord('a')] -= 1
            freq2[ord(s2[r]) - ord('a')] += 1
            l += 1
            r += 1
        
        return freq1 == freq2
