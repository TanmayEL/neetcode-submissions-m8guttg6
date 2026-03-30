class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # prefix, suffix = [0] * n, [0] * n

        # for i in range(n):
        #     if i == 0:
        #         prefix[i] = 1
        #         continue
        #     prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # for i in range(n - 1, -1, -1):
        #     if i == n - 1:
        #         suffix[i] = 1
        #         continue
        #     suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # for i, (p, s) in enumerate(zip(prefix, suffix)):
        #     nums[i] = p * s
        
        # return nums

        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        