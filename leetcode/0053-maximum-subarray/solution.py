class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        sum = 0
        max_sum = nums[0]

        i = 0

        for j in range(n):
            
            sum = max(nums[j], sum+ nums[j])

            max_sum = max(max_sum, sum)

        return max_sum






