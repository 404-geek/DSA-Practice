class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:

        def find_root(n):

            l, r = 0, n

            while l <= r:
                m = (l+r) // 2

                if m ** k <= n:
                    l = m + 1
                else:
                    r = m - 1

            return r

        a = find_root(r)
        b = find_root(l - 1)

        return a - b
