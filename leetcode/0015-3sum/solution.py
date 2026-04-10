class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums = sorted(nums)
        n = len(nums)
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i+1
            r = n - 1

            while l < r:

                to = nums[i] + nums[l] + nums[r]

                if to < 0:
                    l+=1
                elif to > 0:
                    r-=1
                else:
                    res.append([nums[i] , nums[l] , nums[r]])
                    l+=1
                    r-=1

                    while  l < r  and nums[l-1] == nums[l]:
                        l+=1
                    while l < r and nums[r+1] == nums[r]:
                        r-=1
        
        return res
                







        
