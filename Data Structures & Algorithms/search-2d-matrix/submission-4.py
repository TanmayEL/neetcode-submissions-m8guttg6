class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        
        if m >= 1:
            l, r = 0, m - 1
            while l <= r:
                mid = (r + l) // 2
                if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                    row = mid
                    break
                elif target < matrix[mid][0]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        l, r = 0, n - 1
        while l <= r:
            mid = (r + l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l += 1
            else:
                r -= 1
        return False

        #O( m * log(n))
        # n = len(matrix[0])
        # for row in matrix:
        #     if target > row[-1]:
        #         continue
        #     l, r = 0, n - 1
        #     while l <= r:
        #         mid = (r + l) // 2
        #         if row[mid] == target:
        #             return True
        #         elif row[mid] > target:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     break
        # return False