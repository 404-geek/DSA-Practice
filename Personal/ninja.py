class Solution:
    def ninjaTraining(self, matrix):
        n = len(matrix)

        prev = [0] * 4

        prev[0] = max(matrix[0][1], matrix[0][2])
        prev[1] = max(matrix[0][0], matrix[0][2])
        prev[2] = max(matrix[0][0], matrix[0][1])
        prev[3] = max(matrix[0])

        for day in range(1, n):
            curr = [0] * 4

            for last in range(4):
                for task in range(3):
                    if task != last:
                        curr[last] = max(
                            curr[last],
                            matrix[day][task] + prev[task]
                        )

            prev = curr

        return prev[3]