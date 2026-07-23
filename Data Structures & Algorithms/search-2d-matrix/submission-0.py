class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        l = 0
        r = (rows * columns) - 1

        while l <= r:
            m = (l + r) // 2
            row = m // columns
            col = m % columns

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True

        return False