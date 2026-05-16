class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])

        i = 0

        for r in range(rows):
            for c in range(i, cols):
                if r != c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
            i+=1

        for r in range(rows):
            matrix[r].reverse()
