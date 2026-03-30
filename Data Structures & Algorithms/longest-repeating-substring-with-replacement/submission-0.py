class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}

        l = 0
        maxlen = 0

        for r in range(len(s)):
            char = s[r]
            counts[char] = 1 + counts.get(char, 0)
            
            max_count = counts[max(counts, key=lambda k: counts[k])]

            while (r - l + 1) - max_count > k:
                counts[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, (r - l + 1))
        return maxlen



