class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        t = len(tasks)

        tasks = Counter(tasks)

        max_freq = max(tasks.values())

        max_count = 0

        for v in tasks.values():

            if v == max_freq:
                max_count+=1
        
        no_of_intervals = (max_freq - 1) * (n + 1) + max_count

        return max(t, no_of_intervals)









