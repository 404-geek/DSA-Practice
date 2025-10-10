class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        start = 0
        run_sum = 0
        min_len = inf

        for end in range(len(nums)):

            run_sum += nums[end]

            while run_sum >= target:

                min_len = min(min_len, end - start + 1)

                run_sum -= nums[start]

                start+=1

        if min_len == inf:
            return 0
            
        return min_len








        
