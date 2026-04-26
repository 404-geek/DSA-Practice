class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        res = []
        di = Counter(nums)

        for a,b in di.items():

            heapq.heappush(heap, (b,a))

            if len(heap) > k:
                heapq.heappop(heap)

        
        for h in heap:
            res.append(h[1])

        return res

