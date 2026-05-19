class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        x = len(nums)

        nums.sort()

        res = []

        def backtrack(i, path):

            if i == x:
                res.append(path[:])
                return

            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()

            j = i+1

            while j < x and nums[j] == nums[i]:
                j+=1       

            backtrack(j, path)

        backtrack(0,[])

        return res
