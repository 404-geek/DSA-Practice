class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 1 

        while i > 0 and nums[i-1] >= nums[i]:
            i-=1

        if i > 0:
            pivot = i - 1

            j = len(nums) - 1
            while nums[j] <= nums[pivot]:
                j -= 1
            nums[pivot], nums[j] = nums[j], nums[pivot] 
        
        left, right = i, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


        return nums






        




        
