class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr_sum = 0
        max_sum = nums[0]

        for i in nums:

            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum += i

            max_sum = max(curr_sum, max_sum)
            
        
        return max_sum
