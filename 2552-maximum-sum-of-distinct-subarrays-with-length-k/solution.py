class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        i, j = 0, 0

        seen = {}
        max_sum = 0
        temp = 0

        while j < len(nums):

            temp += nums[j]
            seen[nums[j]] = seen.get(nums[j], 0) + 1

            if j-i+1 > k:
                seen[nums[i]] -= 1
                if seen[nums[i]] == 0:
                    del seen[nums[i]]
                temp -= nums[i]
                i+=1


            if j - i +1 == k and len(seen) == k:
                max_sum = max(temp, max_sum)

            j+=1

        return max_sum
