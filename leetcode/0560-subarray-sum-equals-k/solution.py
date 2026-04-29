class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        map = {0:1}
        curr_sum = 0
        ans = 0

        for n in nums:

            curr_sum+=n

            ans += map.get(curr_sum - k, 0)

            map[curr_sum] = map.get(curr_sum, 0) + 1

        return ans



