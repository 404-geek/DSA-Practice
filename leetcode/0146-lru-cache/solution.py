class LRUCache:

    def __init__(self, capacity: int):
        self.bucket = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:

        if key not in self.bucket:
            return -1
        
        self.bucket.move_to_end(key)
        return self.bucket[key]
            

    def put(self, key: int, value: int) -> None:

        self.bucket[key] = value
        self.bucket.move_to_end(key)

        if len(self.bucket) > self.capacity:
            self.bucket.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
