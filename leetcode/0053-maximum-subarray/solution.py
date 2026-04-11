class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        runn_sum = nums[0]
        best = nums[0]

        for i in range(1,n):

            runn_sum  = max(nums[i], runn_sum + nums[i])

            best = max(runn_sum , best)

        return best



