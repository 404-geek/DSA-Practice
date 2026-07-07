class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        @cache
        def dfs(i, s):

            if s == target:
                return True

            if s > target:
                return False

            if i >= n:
                return False

            return dfs(i+1, nums[i] + s) or dfs(i+1, s)

        return dfs(0, 0)






            
