class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n = len(nums2)
        m = len(nums1)
        map = {}
        res = []

        stack = [nums2[-1]]

        for i in range(n - 2, -1, -1):
                
            while stack and stack[-1] < nums2[i]:
                stack.pop()

            if stack:
                map[nums2[i]] = stack[-1]

            stack.append(nums2[i])
            

        for num in nums1:

            if num in map:
                res.append(map[num])

            else:
                res.append(-1)

        return res



        


            


