class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if len(nums) <= k:

            return [max(nums)]


        q = deque()

        start = 0

        res = []

        for end in range(len(nums)):

            while q and nums[q[-1]] < nums[end]:
                q.pop()

            q.append(end)

            if q[0] < start:

                q.popleft() 
            
            if end - start + 1 == k:

                res.append(nums[q[0]])

                start+=1

        return res




        
