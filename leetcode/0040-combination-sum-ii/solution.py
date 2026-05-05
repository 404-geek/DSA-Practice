class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates)

        candidates.sort()
        res = []
        
        def traverse(i, su, arr):

            if su == 0:
                res.append(arr[:])
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                if candidates[j] > su:
                    break

                arr.append(candidates[j])
                traverse(j+1, su - candidates[j], arr)
                arr.pop()

        traverse(0, target, [])

        return res

