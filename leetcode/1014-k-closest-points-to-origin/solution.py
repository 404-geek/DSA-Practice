class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        res = []
        for x,y in points:

            a = x*x + y*y

            heapq.heappush(heap, (-a, [x,y]))

            if len(heap) > k:
                heapq.heappop(heap)


        for a, h in heap:
            res.append(h)
        
        return res


