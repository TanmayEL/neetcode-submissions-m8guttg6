class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}

        l = 0
        maxlen = 0
        maxFreq = 0

        for r in range(len(s)):
            char = s[r]

            count_add = 1 + counts.get(char, 0)
            maxFreq = max(maxFreq, count_add)

            counts[char] = count_add

            while (r - l + 1) - maxFreq > k:
                counts[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, (r - l + 1))
        return maxlen



