class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Brute Force O(n + m) for both
        n = len(nums1)
        m = len(nums2)

        arr = [0] * (n+m)

        i = 0

        l, r = 0, 0

        while l < n and r < m:
            if nums1[l] <= nums2[r]:
                arr[i] = nums1[l]
                l += 1
                i += 1
            else:
                arr[i] = nums2[r]
                r += 1
                i += 1
        
        while l < n:
            arr[i] = nums1[l]
            l += 1
            i += 1
        
        while r < m:
            arr[i] = nums2[r]
            r += 1
            i += 1
        
        median = arr[(n + m) // 2] if (n + m) % 2 == 1 else (arr[(n + m)//2] + arr[(n + m) // 2 - 1]) / 2
        
        return median
            