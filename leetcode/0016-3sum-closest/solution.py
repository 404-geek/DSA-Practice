class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            l = i + 1
            r = n - 1

            while l < r:

                su = nums[i] + nums[l] + nums[r]

                if abs(su - target) < abs(closest-target):
                    closest = su

                if su < target:
                    l+=1
                
                elif su > target:
                    r-=1
                
                else:
                    return target

        return closest



