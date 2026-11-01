class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:

        n = len(nums)

        su = sum(nums)

        rem = su % p

        if rem == 0:
            return 0

        mp = {0:-1}

        min_len = float("inf")

        prefix_sum = 0

        for i in range(n):

            prefix_sum += nums[i]

            current_rem = prefix_sum % p

            tar = (current_rem - rem) % p

            if tar in mp:

                min_len = min(min_len, i - mp[tar])
            
            mp[current_rem] = i

        return -1 if min_len >= n else min_len
 
            
        
