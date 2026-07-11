class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        arr = [[] for _ in range(n)]

        for flight in flights:

            start, stop, cost = flight

            arr[start].append((stop, cost))
        
        @cache
        def track(stop, k):

            if stop == dst:
                return 0

            if k == 0:
                return float("inf")

            total = float("inf")

            for s,c in arr[stop]:

                remaining_cost = track(
                    s,
                    k- 1
                )

                total = min(
                    total,
                    c + remaining_cost
                )

            return total
            
        a = track(src, k+1)

        if a != float("inf"):
            return a
        else:
            return -1



        
