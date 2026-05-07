class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        nums = [i for i in range(1, n+1)]

        k = k - 1

        ans = []

        while n > 0:

            f = math.factorial(n-1)

            ind = k // f

            ans.append(nums[ind])

            nums.pop(ind)

            n-=1

            k = k % f

        return "".join(str(i) for i in ans)





















 

            




        
