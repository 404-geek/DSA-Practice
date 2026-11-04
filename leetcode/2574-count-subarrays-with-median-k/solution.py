from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mid = nums.index(k)

        freq = defaultdict(int)
        freq[0] = 1

        # Step 1: Calculate balances to the left of k
        balance = 0

        for i in range(mid - 1, -1, -1):
            if nums[i] > k:
                balance += 1
            else:
                balance -= 1

            freq[balance] += 1

        # Step 2: Calculate balances to the right of k
        balance = 0
        count = 0

        for j in range(mid, n):
            if nums[j] > k:
                balance += 1
            elif nums[j] < k:
                balance -= 1

            # Total balance must be 0 or 1
            count += freq[-balance] + freq[1 - balance]

        return count
