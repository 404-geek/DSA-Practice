class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()

        i = 0
        total = 0
        ans = 0

        for n in range(len(nums)):

            total += nums[n]

            while nums[n] * (n - i + 1) - total > k:

                total -= nums[i]

                i+=1

            ans = max(ans, n - i + 1)

        return ans

            
        

