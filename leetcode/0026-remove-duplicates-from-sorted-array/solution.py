class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = i + 1
        cnt = 0

        while j < len(nums):

            if nums[i] < nums[j]:
                cnt += 1
                nums[cnt] = nums[j]
                i = cnt

            j += 1

        return cnt+1
        
