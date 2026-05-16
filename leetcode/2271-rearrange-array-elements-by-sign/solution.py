class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0] * n

        pos = 0
        neg = 1

        for nu in nums:
            if nu >= 0:
                res[pos] = nu
                pos+=2
            else:
                res[neg] = nu
                neg+=2

        return res
        
