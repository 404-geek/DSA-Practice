class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        pref = 1
        suff = 1
        n = len(nums)
        max_p = nums[0]

        for i in range(n):

            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1

            pref *= nums[i]
            suff *= nums[n- i - 1]
            
            max_p = max(max_p, max(pref, suff))

        return max_p

                



