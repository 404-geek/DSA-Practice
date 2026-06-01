class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        ans = 0

        for l in range(n):

            balance = 0

            for r in range(l, n):

                if nums[r] == target:
                    balance +=1
                else:
                    balance-=1

                if balance > 0:
                    ans+=1

        return ans


