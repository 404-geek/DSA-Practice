class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0] * (n)
        ans = 0

        if n == 1:
            return nums[0]

        for m in range(n):

            dp[m] = max(nums[m] + dp[m-2], dp[m-1])
            print(dp)

        return dp[-1]



