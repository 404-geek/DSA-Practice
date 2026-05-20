class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        res = []

        def gen_perm(i, nums):
                
            if i == n:
                res.append(nums[:])
                return

            seen = set()

            for j in range(i, n):

                if nums[j] in seen:
                    continue

                seen.add(nums[j])

                nums[i], nums[j] = nums[j], nums[i]

                gen_perm(i+1, nums)

                nums[j], nums[i] = nums[i], nums[j]

        gen_perm(0, nums)

        return res



        
