class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # Anything left in stack has no next greater
        for num in stack:
            next_greater[num] = -1

        # Lookup for nums1
        return [next_greater[num] for num in nums1]

        
