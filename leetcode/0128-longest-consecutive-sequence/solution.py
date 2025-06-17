class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        set_nums = set(nums)
        max_cnt = 0

        for i in set_nums:
            if i - 1 not in set_nums:  # only start from the beginning of a sequence
                cnt = 1
                current = i
                while current + 1 in set_nums:
                    current += 1
                    cnt += 1
                max_cnt = max(max_cnt, cnt)

        return max_cnt

                






        

