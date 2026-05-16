class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        curr = 0

        for j in nums:

            curr += j
            max_sum = max(max_sum, curr)

            if curr < 0:
                curr = 0

        return max_sum



