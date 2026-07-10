class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n_len = len(nums)
        ans = [-1] * n_len

        stack = []

        for n in range(2 * n_len - 1, -1, -1):

            val = nums[n % n_len]

            while stack and val >= stack[-1]:
                stack.pop()

            if stack and n < n_len:
                ans[n] = stack[-1]

            stack.append(val)

        return ans
    
                      

        
