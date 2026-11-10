from bisect import insort

class Allocator:

    def __init__(self, n: int):

        self.ranges = []
        self.total = n

    def allocate(self, size: int, mID: int) -> int:

        start = 0

        for a, b, owner in self.ranges:
            if a-start >= size:
                break
            start = b

        if start + size > self.total:
            return -1
        
        insort(self.ranges, (start, start + size, mID))

        return start

    def freeMemory(self, mID: int) -> int:

        rem = []

        freed = 0

        for start, end, owner in self.ranges:
            if owner == mID:
                freed+=end-start
            else:
                rem.append((start,end,owner))

        self.ranges = rem
        return freed



    

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
