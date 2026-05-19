class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        n = len(candidates)

        def find_target(path, i, su):

            if su == target:
                res.append(path[:])
                return

            if i == n or su > target:
                return

            if su + candidates[i] > target:
                return

            path.append(candidates[i])
            find_target(path, i, su + candidates[i])
            path.pop()
            find_target(path, i+ 1, su)
        
        find_target([], 0, 0)

        return res

        
