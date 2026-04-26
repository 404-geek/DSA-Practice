class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        n = len(candidates)

        def ssum(i, target, path):

            if target == 0:
                res.append(path[:])
                return
            
            if i == n or target < 0:
                return

            path.append(candidates[i])
            ssum(i, target - candidates[i], path)
            path.pop()

            ssum(i+1, target, path)

        ssum(0, target, [])

        return res

            
            


