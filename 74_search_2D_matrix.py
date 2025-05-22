class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        target_row = 0

        # binary search for target row
        l, r = 0, row - 1
        while l <= r:
            m = l + (r - l)//2
            if matrix[m][0] <= target <= matrix[m][-1]:
                target_row = m
                break
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        
        # binary search for target in target row
        l, r = 0, col - 1
        while l <= r:
            m = l + (r - l)//2
            if matrix[target_row][m] == target:
                return True
            elif matrix[target_row][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
