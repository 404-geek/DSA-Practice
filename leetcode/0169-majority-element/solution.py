class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        curr = None
        vote = 0

        for i in range(len(nums)):

            if vote == 0:
                curr = nums[i]
                vote+=1

            elif nums[i] == curr:
                vote+=1
            else:
                vote-=1

        return curr

                
