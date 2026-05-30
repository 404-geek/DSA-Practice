class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n <= 2:
            return max(nums)

        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])

        for i in range(2, n):

            c = max(nums[i] + prev1, prev2)
            prev1 = prev2
            prev2 = c
            
        return prev2
