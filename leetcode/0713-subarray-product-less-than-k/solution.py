class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k == 0:
            return 0

        start = 0

        run_prod = 1

        cnt = 0

        for end in range(len(nums)):

            run_prod *= nums[end]

            while start <= end and run_prod >= k:
                run_prod //= nums[start]
                start += 1

            cnt += end - start + 1

        return cnt
            
            


                
        
