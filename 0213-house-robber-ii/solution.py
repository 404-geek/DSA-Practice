class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def linear(arr):
            rob, not_rob = 0,0

            for i in arr:

                new_rob = not_rob + i

                not_rob = max(rob, not_rob)

                rob = new_rob

            return max(rob, not_rob)

        if len(nums) == 1:

            return nums[0]

        return max(linear(nums[:-1]), linear(nums[1:]))
