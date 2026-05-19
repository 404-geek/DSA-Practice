class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        n = len(candidates)

        def find_target(path, start, su):

            if su == target:
                res.append(path[:])
                return
            
            if su  > target:
                return

            for i in range(start, n):

                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if su + candidates[i] > target:
                    break

                path.append(candidates[i])
                find_target(path, i+ 1, su + candidates[i])
                path.pop()
        
        find_target([], 0, 0)

        return res
