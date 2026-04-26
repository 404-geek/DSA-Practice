class RandomizedSet:

    def __init__(self):

        self.pos = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.arr.append(val)
        self.pos[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:

        if val in self.pos:
            w = self.pos[val]
            last_val = self.arr[-1]

            self.arr[w] = last_val
            self.pos[last_val] = w

            self.arr.pop()
            del self.pos[val]
            
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
