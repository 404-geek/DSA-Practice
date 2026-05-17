class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        if len(nums) < 4:
            return []

        n = len(nums)

        nums.sort()
        # print(nums)

        res = []

        for i in range(n-3):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            a = nums[i]

            # print("i")
            # print(i)
            
            for j in range(i+1, n-2):

                # print(i, j)

                if j > i+1 and nums[j] == nums[j-1]:
                    # print("here")
                    continue

                b = nums[j]

                # print("b")
                # print(b)

                l = j + 1
                r = n - 1

                while l < r:

                    # print(nums[l], nums[r])

                    su = a + b + nums[l] + nums[r]

                    if su < target:
                        l+=1
                    
                    elif su > target:
                        r-=1

                    else:
                        res.append([a,b,nums[l], nums[r]])

                        l+=1
                        r-=1

                        while l < r and nums[l] == nums[l-1]:
                            l+=1
                        while l < r and nums[r] == nums[r+1]:
                            r-=1

        return res
        
