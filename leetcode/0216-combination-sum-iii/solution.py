class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []

        def back(i, target, path):

            if len(path) == k:
                if target == 0:
                    res.append(path[:])
                return

            for j in range(i,10):

                path.append(j)
                back(j+1, target - j, path)
                path.pop()

        back(1, n, [])

        return res

                


