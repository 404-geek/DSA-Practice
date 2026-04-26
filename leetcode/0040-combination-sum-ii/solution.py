class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        n = len(candidates)
        
        candidates.sort()

        def back(rem, target, path):

            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return

            for i in range(len(rem)):

                if i > 0 and rem[i] == rem[i - 1]:
                    continue

                path.append(rem[i])
                back(rem[i+1:], target - rem[i], path)
                path.pop()


        back(candidates, target, [])

        return res
