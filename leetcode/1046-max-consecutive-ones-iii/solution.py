class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zero_cnt = 0

        i = 0

        maxl = 0

        for j in range(len(nums)):

            if nums[j] == 0:
                zero_cnt += 1

            while zero_cnt > k:

                if nums[i] == 0:
                    zero_cnt-=1
                i+=1
            
            maxl = max(maxl , j - i + 1)

        return maxl
                
        
