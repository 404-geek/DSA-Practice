class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        cnt = 0
        curr_val = nums[0]

        for n in nums:

            if cnt == 0:
                cnt = 1
                curr_val = n

            elif n == curr_val:
                cnt+=1
            else:
                cnt-=1

        return curr_val
                
        
        
