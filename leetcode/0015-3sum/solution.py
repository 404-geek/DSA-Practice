class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        n= len(nums)
        nums.sort()
        res = []

        print(nums)

        for i in range(0, n-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = n-1

            while l < r:
                
                su = nums[i] + nums[l] + nums[r]

                if su < 0:
                    l+=1
                
                elif su > 0:
                    r-=1
                
                else:

                    res.append([nums[i], nums[l] , nums[r]])
                    l+=1
                    r-=1

                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r+1] == nums[r]:
                        r-=1


        return res

            

