class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        run_sum = 0

        map = {0:-1}

        for i, v in enumerate(nums):

            run_sum += v

            l = run_sum % k

            if l in map:
                if i - map[l] >= 2:
                    return True
            else:
                map[l] = i
        
        return False
