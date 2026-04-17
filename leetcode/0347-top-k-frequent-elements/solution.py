class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = Counter(nums)

        print(d)
        ans = []

        heap = []

        for  a, b in d.items():

            heapq.heappush(heap, (b, a))

            if len(heap) > k:
                heapq.heappop(heap)


        for freq, num in heap:

            ans.append(num)

        return ans
