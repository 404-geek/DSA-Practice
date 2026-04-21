class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(ind, target, path):

            if target == 0:
                res.append(path[:])
                return

            if ind == len(candidates) or target < 0:
                return
             
            path.append(candidates[ind])
            backtrack(ind, target-candidates[ind], path)
            path.pop()

            backtrack(ind + 1, target, path)

        backtrack(0, target, [])
        return res


        
