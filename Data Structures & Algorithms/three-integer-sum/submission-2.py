class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # # -4, -1, -1, 0, 1, 2
        # n = len(nums)
        # ans = []

        # for i in range(n):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     if nums[i] > 0:
        #         return ans
        #     l, r = i + 1, n - 1
        #     while l < r:
        #         threeSum = nums[i] + nums[l] + nums[r]
        #         if threeSum == 0:
        #             ans.append([nums[i], nums[l], nums[r]])
        #             l += 1
        #             while l < n and nums[l] == nums[l - 1]:
        #                 l += 1
        #         elif threeSum < 0:
        #             l += 1
        #             while l < n and nums[l] == nums[l - 1]:
        #                 l += 1
        #         else:
        #             r -= 1
        # return ans

        nums.sort()
        n = len(nums)
        res = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            if nums[i] > 0:
                break
            
            l, r = i + 1, n - 1
            while l < r:

                if num + nums[l] + nums[r] == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    
                else:
                    r -= 1
            
        return res
























