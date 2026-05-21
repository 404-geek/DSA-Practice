class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        hp = []

        for n in arr:

            v = abs(x-n)

            heapq.heappush(hp, (-v, -n))

            while len(hp) > k:
                heapq.heappop(hp)


        return sorted([-a[1] for a in hp])

            


        