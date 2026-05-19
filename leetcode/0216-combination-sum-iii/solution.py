class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        def find_sum(path, a, j, su):

            if a == 0:
                if su == n:
                    print("here")
                    res.append(path[:])
                return

            for i in range(j, 10):
                if su + i > n:
                    break
                path.append(i)
                find_sum(path, a - 1, i+1, su+i)
                path.pop()

        find_sum([], k,1, 0)
        return res

