class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) - 1, len(matrix[0]) - 1

        top, bottom = 0, row

        
        # print(mid, matrix[mid])
        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            if target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        
        if not (top <= bottom):
            return False
        row = (top + bottom) // 2
        print(row)
        l, r = 0, col
        while l <= r:
            m = (l + r) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False
        
