class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_first():
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        def find_last(l):
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l - 1

        first = find_first()

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = find_last(first)
        return [first, last]
