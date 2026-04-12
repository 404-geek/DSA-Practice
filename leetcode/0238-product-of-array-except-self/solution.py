class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        res = [1] * n

        prefix = 1

        for j in range(n):

            res[j] = prefix
            prefix *= nums[j]

        suffix = 1

        for k in range(n-1, -1, -1):

            res[k] *= suffix

            suffix *= nums[k] 


        return res

         

