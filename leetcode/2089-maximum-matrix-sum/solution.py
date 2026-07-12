class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        cnt_neg = 0
        su = 0
        min_element = float("inf")

        for r in range(rows):
            for c in range(cols):

                val = matrix[r][c]

                min_element = min(abs(val), min_element)

                su += abs(val)

                if val < 0:
                    cnt_neg+=1

        if cnt_neg % 2 == 0:
            return su
        
        else:
            return su - 2 * min_element


                
        
