class Solution:
    def check(self, nums: List[int]) -> bool:

        l = len(nums)
        cnt = 0
        
        for i in range(1, 2*l):
            if nums[(i-1) % l] <= nums[i % l]:
                cnt+=1
            else:
                cnt=1
            if cnt == l:
                return True

        return False
            
        
