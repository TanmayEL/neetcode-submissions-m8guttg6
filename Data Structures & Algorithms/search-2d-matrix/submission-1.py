class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        for row in matrix:
            if target > row[-1]:
                continue
            l, r = 0, m - 1
            while l <= r:
                mid = (r + l) // 2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            break
        return False