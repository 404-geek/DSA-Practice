class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums = sorted(nums)

        n = len(nums)

        res = []


        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+ 1
            r = n - 1

            while l < r:

                su = nums[i] + nums[l] + nums[r]

                if su < 0:
                    l+=1
                elif su > 0:
                    r-=1
                              
                else:

                    res.append([nums[i] , nums[l] , nums[r]])

                    l+=1
                    r-=1

                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
                    
                    while nums[r] == nums[r + 1] and l < r:
                        r-=1


        return res





                







        
