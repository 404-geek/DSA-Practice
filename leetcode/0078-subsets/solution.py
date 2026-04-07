class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(i, path):

            res.append(path[:])

            for n in range(i, len(nums)):

                path.append(nums[n])
                backtrack(n+1, path)
                path.pop()

        
        backtrack(0,[])

        return res

        
