class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()

        print(nums)

        res = 0
        mod = (10**9 + 7)

        l = 0 
        r = len(nums) - 1

        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res +  pow (2, (r - l), mod)) % mod
                l+=1
            else:
                r-=1

        return res







                


        
