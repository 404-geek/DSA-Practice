class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n_len = len(nums)
        ans = [-1] * n_len

        stack = []

        for n in range(2 * n_len):

            val = nums[n % n_len]

            while stack and val > nums[stack[-1]]:
                ix = stack.pop()
                ans[ix] = val
            
            if n < n_len:
                stack.append(n)

        return ans            

        
