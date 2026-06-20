class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_row(l, r, matrix, target):
            if l > r:
                return False
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                return find_target(0, len(matrix[m]) - 1, matrix[m], target)
            if target < matrix[m][0]:
                return find_row(l, m - 1, matrix, target)
            if target > matrix[m][-1]:
                return find_row(m + 1, r, matrix, target)
            return False
        def find_target(l, r, row, target):
            if l > r:
                return False
            m = (l + r) // 2
            if target == row[m]:
                return True
            if target < row[m]:
                return find_target(l, m - 1, row, target)
            if target > row[m]:
                return find_target(m + 1, r, row, target)
        return find_row(0, len(matrix) - 1, matrix, target)