class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {}
        count[0] = 1
        prefix = 0
        res = 0

        for num in nums:
            prefix += num
            res += count.get(prefix - k, 0)
            count[prefix] = 1 + count.get(prefix, 0)
        
        return res