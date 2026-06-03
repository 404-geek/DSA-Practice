class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        pref_prd = 1
        suff_prd = 1

        n = len(nums)
        max_prd = nums[0]

        for i in range(n):

            val_pref = nums[i]
            val_suff = nums[n-i-1]

            pref_prd *= val_pref
            suff_prd *= val_suff

            max_prd = max(max_prd, pref_prd, suff_prd)
            
            if val_pref == 0:
                pref_prd = 1
            
            if val_suff == 0:
                suff_prd = 1

        return max_prd

            
            

        
