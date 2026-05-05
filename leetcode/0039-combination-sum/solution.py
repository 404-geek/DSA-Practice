class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        n = len(candidates)

        def traverse(i, su, arr):

            if su == 0:
                res.append(arr[:])
                return
            
            if i == n:
                return

            if candidates[i] <= su:
                arr.append(candidates[i])
                traverse(i, su - candidates[i], arr)
                arr.pop()

            traverse(i+1, su, arr)


        traverse(0, target, [])

        return res




        



        




        
        
