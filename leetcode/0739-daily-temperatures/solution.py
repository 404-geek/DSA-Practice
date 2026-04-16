class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)

        stack = []

        ans = [0] * n

        for i in range(n):

            curr = temperatures[i]

            while stack and curr > temperatures[stack[-1]]:

                idx = stack.pop()
                ans[idx] = i - idx
            
            stack.append(i)
        
        return ans
        
