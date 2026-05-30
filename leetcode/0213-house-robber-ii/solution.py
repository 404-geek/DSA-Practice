class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        def robr(nums):

            n = len(nums)

            prev1 = nums[0]
            prev2 = max(prev1, nums[1])

            for i in range(2, n):

                curr = max(prev2, nums[i] + prev1)
                prev1 = prev2
                prev2 = curr
                
            return prev2

        return max(robr(nums[1:]),  robr(nums[:-1]))
        
        
