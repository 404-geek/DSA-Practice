class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def find_whether(max_sum):

            s = 0
            g = 1

            for n in nums:

                if s + n <= max_sum:
                    s += n
                else:
                    g+=1
                    s = n
            
            return g <= k

        l = max(nums)
        r = sum(nums)

        while l < r:

            mid = (l+r) // 2

            if find_whether(mid):

                r = mid
            
            else:
                l = mid + 1

        return l






        

