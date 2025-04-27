class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        # helper to rob a linear street
        def rob_linear(nums):
            prev1 = 0
            prev2 = 0
            for num in nums:
                temp = prev1
                prev1 = max(prev1, prev2 + num)
                prev2 = temp
            return prev1
        
        # either rob 0..n-2 or rob 1..n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))



        
