class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        one = 0
        zero = 0
        res = 0

        diff = {}

        for i, k in enumerate(nums):

            if k == 0:
                zero+=1
            if k == 1:
                one+=1
            
            if one - zero not in diff:
                diff[one-zero] = i

            if one == zero:
                res = one + zero
            
            else:
                idx = diff[one-zero]
                res = max(res, i-idx)

        return res
