class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = 0
        index = 0

        for ind, row in enumerate(mat):
            temp_ones = sum(row)

            if temp_ones > max_ones:
                max_ones = temp_ones
                index = ind
            
        return [index, max_ones]


            

            
            
