class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        def count(prefix, n):

            count = 0
            curr = prefix
            next = prefix+1

            while curr <= n:
                count += min(n+1, next) - curr
                curr*=10
                next *=10
            
            return count

        curr = 1
        k -= 1

        while k > 0:

            val = count(curr, n)

            if val <= k:
                curr+=1
                k-=val
            else:
                curr *=10
                k-=1

        return curr
            

