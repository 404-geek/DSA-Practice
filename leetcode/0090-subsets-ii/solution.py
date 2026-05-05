class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        x = len(nums)

        nums.sort()

        res = []

        def backtrack(i, path):

            res.append(path[:])

            for n in range(i, x):

                if n > i and nums[n] == nums[n-1]:
                    continue

                path.append(nums[n])
                backtrack(n+1, path)
                path.pop()
\

        backtrack(0,[])

        return res
