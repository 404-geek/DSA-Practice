class LRUCache:

    def __init__(self, capacity: int):

        self.lru = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.move_to_end(key)
        
        return self.lru.get(key, -1)

    def put(self, key: int, value: int) -> None:

        self.lru[key] = value
        self.lru.move_to_end(key)

        if len(self.lru) > self.capacity:
            self.lru.popitem(last=False)
        

        
