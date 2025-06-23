class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        pre, suf  = 1,1

        for i in range(len(nums)):

            res[i] = pre

            pre *= nums[i]

        
        for i in  reversed(range(len(nums))):

            res[i] *= suf
            suf *= nums[i]

        return res


        
