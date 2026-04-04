class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)

        def count(x, n):

            row = n - 1
            col = 0
            count = 0

            while row >= 0 and col < n:

                if matrix[row][col] <= x:
                    count += row + 1
                    col+=1
                else:
                    row -= 1

            return count

        l = matrix[0][0]
        r = matrix[-1][-1]

        while l < r:

            mid = (l + r) // 2

            if count(mid, n) < k:

                l = mid + 1
            
            else:

                r = mid

        return l


