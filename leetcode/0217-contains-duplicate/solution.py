class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        m = set()

        for i in nums:
            if i in m:
                return True
            m.add(i)

        return False
        
