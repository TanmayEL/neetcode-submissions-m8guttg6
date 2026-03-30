class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            count = ''
            while s[i] != '#':
                count += str(s[i])
                i += 1
            res.append(s[i + 1: i + int(count) + 1])
            i += int(count) + 1
        return res