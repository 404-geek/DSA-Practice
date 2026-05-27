class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        res = sorted(nums)
        n = len(nums)

        mid = (n + 1) // 2

        small = res[:mid][::-1]
        large = res[mid:][::-1]

        nums[::2] = small
        nums[1::2] = large






                    
