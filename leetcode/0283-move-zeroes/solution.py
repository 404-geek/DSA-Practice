class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[next], nums[i] = nums[i], nums[next]
                next+=1
        
        return nums


        
