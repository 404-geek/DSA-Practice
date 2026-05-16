class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n = len(nums)

        freq = [0] * n

        for n in nums:

            freq[n]+=1

            if freq[n] == 2:
                return n 
