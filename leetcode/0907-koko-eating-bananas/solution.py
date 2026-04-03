class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def find_time_required(rate):

            time = 0
            for i in piles:

                time+= ceil(i/rate)

            return time

        l = 1
        r = max(piles)

        while l < r:

            mid = (l + r) // 2

            if find_time_required(mid) > h:
                l = mid+1

            else:
                r = mid

        return l
        




        
        
