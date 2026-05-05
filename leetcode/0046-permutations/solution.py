class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        res = []
        
        def traverse(i):

            if i == n:
                res.append(nums[:])
                return

            for j in range(i, n):

                nums[i], nums[j] = nums[j], nums[i]
                traverse(i+1)
                nums[j], nums[i] = nums[i], nums[j]

        traverse(0)

        return res
