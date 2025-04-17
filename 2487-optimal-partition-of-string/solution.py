class Solution:
    def partitionString(self, s: str) -> int:
        part_set = set()
        part = 0
        for char in s:
            
            if char in part_set:
                part+=1
                part_set.clear()
            part_set.add(char)
        

        return part + 1
