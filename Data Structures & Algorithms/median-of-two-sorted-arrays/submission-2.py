class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        # [1, 3, 5, 6, 9]
        # [2, 3, 4, 5, 5]
        total = len1 + len2
        half = total // 2

        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        
        l, r = 0, len(nums1) - 1

        while True:
            mid = (r + l) // 2
            other_mid = half - mid - 2

            left_nums1 = nums1[mid] if mid >= 0 else float('-inf')
            right_nums1 = nums1[mid + 1] if (mid + 1) < len1 else float('inf')
            left_nums2 = nums2[other_mid] if other_mid >= 0 else float('-inf')
            right_nums2 = nums2[other_mid + 1] if (other_mid + 1) < len2 else float('inf')

            if left_nums1 <= right_nums2 and left_nums2 <= right_nums1:

                if total % 2:
                    return min(right_nums1, right_nums2)
                return (max(left_nums1, left_nums2) + min(right_nums1, right_nums2)) / 2
                    
            elif left_nums1 > right_nums2:
                r = mid - 1
            else:
                l = mid + 1
