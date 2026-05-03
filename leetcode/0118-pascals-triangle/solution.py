class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1]]

        for i in range(2, numRows + 1):

            temp = res[-1]
            f = [1]

            t = len(temp)

            for j in range(1, t):

                s = f[-1] + j
                f.append(temp[j-1] + temp[j])

            f.append(1)         
            
            res.append(f)
        
        return res



