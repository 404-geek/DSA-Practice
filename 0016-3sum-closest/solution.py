class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        target_sum = 0
        dist = float("inf")

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums) -1

            while left < right:

                t_sum = nums[i] + nums[left] + nums[right]

                if abs(target - t_sum) < dist:
                    dist = abs(target - t_sum)
                    target_sum = t_sum
                
                if t_sum == target:
                    return t_sum

                if t_sum < target:
                    left+=1

                else:
                    right-=1

        
        return target_sum





        
