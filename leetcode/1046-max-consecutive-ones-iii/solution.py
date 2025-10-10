class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        start = 0
        max_sub = 0
        zer_count = 0

        for end in range(len(nums)):

            if nums[end] == 0:
                zer_count+=1

            while zer_count > k:            

                if nums[start] == 0:
                    zer_count-=1
                start+=1

            max_sub = max(max_sub, end - start + 1)

        return max_sub




            
        
