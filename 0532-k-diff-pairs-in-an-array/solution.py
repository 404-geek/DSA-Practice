class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        j = 1
        cnt = 0

        while i < len(nums) and j < len(nums):

            if i == j  or nums[j] - nums[i] < k:
                j+=1
            
            elif nums[j] - nums[i] > k:
                i+=1
            else:
                cnt+=1
                i+=1
                j+=1

                while i < len(nums) and nums[i] == nums[i-1]:
                    i+=1
                while j < len(nums) and nums[j] == nums[j-1]:
                    j+=1


        return cnt
