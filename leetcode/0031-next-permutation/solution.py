class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(l, r):

            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        
        n = len(nums)
        br = -1

        for i in range(n-2, -1, -1):

            if nums[i] < nums[i+1]:
                br = i
                break

        if br == -1:
            return nums.reverse()

        for j in range(n -1, br , -1):
            if nums[j] > nums[br]:
                nums[br], nums[j] = nums[j], nums[br]
                break

        reverse(br + 1, n - 1)
