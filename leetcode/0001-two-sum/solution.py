class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        freq = {}

        for ind, num in enumerate(nums):
            
            find = target - num

            if find in freq:
                return [freq[find], ind]
            
            freq[num] = ind
