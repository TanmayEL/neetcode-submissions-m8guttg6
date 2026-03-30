class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # -4, -1, -1, 0, 1, 2
        n = len(nums)
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                return ans
            l, r = i + 1, n - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < n and nums[l] == nums[l - 1]:
                        l += 1
                elif threeSum < 0:
                    l += 1
                    while l < n and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
        return ans