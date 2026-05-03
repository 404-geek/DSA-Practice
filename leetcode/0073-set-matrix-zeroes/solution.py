class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])

        mark_rows = [0] * rows
        mark_cols = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    mark_rows[i] = 1
                    mark_cols[j] = 1

        for i in range(rows):
            for j in range(cols):

                if mark_rows[i] == 1 or mark_cols[j] == 1:
                    matrix[i][j] = 0
        
        return matrix

