class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        r_max = [0] * n
        r_max[-1] = nums[-1]
        ans = 0

        for i in range(n-2, -1, -1):

            r_max[i] = max(nums[i], r_max[i+1])

        i = 0
        j = 0
        
        while j < n:
            if nums[i] <= r_max[j]:
                ans = max(ans, j - i)
                j+=1
            else:
                i+=1

        return ans
            
            

        
        
