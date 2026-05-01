class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        window = []

        for i, num in enumerate(nums):

            pos = bisect_left(window, num - valueDiff)

            if pos < len(window) and window[pos] <= num + valueDiff:
                return True

            insort(window, num)

            if i >= indexDiff:
                old = nums[i-indexDiff]
                old_pos = bisect_left(window,old)
                window.pop(old_pos)
        
        return False
