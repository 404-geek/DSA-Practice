class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        left = 0
        max_sum = 0
        curr_sum = 0
        vi = set()

        for right in range(len(nums)):

            while nums[right] in vi:
                vi.remove(nums[left])
                curr_sum -= nums[left]
                left+=1
            
            vi.add(nums[right])
            curr_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum,  curr_sum)
                vi.remove(nums[left])
                curr_sum -= nums[left]
                left+=1

        return max_sum 
        
                    


        
