class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        n = len(nums)
        print(n)

        if n < k:
            return max(nums)

        res = []

        for i in range(n):

            if q and q[0] <= i - k:
                q.popleft()

            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])

        return res
        
