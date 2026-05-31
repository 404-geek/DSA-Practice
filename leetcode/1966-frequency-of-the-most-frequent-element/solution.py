class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()

        n = len(nums)
        tot = 0
        i = 0
        max_freq = 0

        for j in range(n):
 
            tot += nums[j]

            while (j - i + 1) * nums[j] - tot > k:

                tot -= nums[i]

                i+=1

            max_freq = max(j - i + 1, max_freq)

        return max_freq

            


        
