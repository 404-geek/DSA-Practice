class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        n = len(nums)
        mem = {}

        def back(target):

            if target == 0:
                return 1

            if target < 0:
                return 0
            
            if target in mem:
                return mem[target]

            cnt = 0

            for i in nums:
                cnt += back(target - i)

            mem[target] = cnt

            return cnt

        return back(target)



