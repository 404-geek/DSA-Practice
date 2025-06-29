class RandomizedSet:

    def __init__(self):

        self.nums = []
        self.index = {}
        

    def insert(self, val: int) -> bool:

        if val not in self.index:

            self.nums.append(val)
            self.index[val] = len(self.nums) - 1

            return True
        
        else:
            return False
        

    def remove(self, val: int) -> bool:

        if val in self.index:


            ind = self.index.get(val)
            last_element = self.nums[-1]

            self.nums[ind] = last_element
            self.nums.pop()
            self.index[last_element] = ind
            del self.index[val]

            return True
        
        else:

            return False
        

    def getRandom(self) -> int:


        return random.choice(self.nums)
        



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
