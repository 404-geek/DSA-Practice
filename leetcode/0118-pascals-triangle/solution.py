class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1]]

        for i in range(1, numRows):

            m = res[-1]

            temp = [1]

            for i in range(1, len(m)):

                temp.append(m[i] + m[i-1])

            temp.append(1)

            res.append(temp)

        return res

        
