class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minElement = 1001
        while l <= r:
            mid = (l + r) // 2
            n = nums[mid]
            minElement = min(minElement, n)

            if n >= nums[0] and n <= nums[-1]:
                return nums[0]
            elif n >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        return minElement
