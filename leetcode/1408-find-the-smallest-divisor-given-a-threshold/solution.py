class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:


        def find_sum(x):

            sum = 0

            for n in nums:

                sum += ceil(n / x)

            return sum > threshold


        l = 1
        r = max(nums)


        while l < r:

            mid = (l + r) // 2

            if find_sum(mid):

                l = mid + 1
            
            else:

                r = mid

        return l

        
