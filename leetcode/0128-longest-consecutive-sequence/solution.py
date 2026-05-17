class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n_set = set(nums)
        max_seq = 0

        for n in n_set:

            if n - 1 not in n_set:

                curr = n
                seq = 1

                while curr + 1 in n_set:
                    curr+=1
                    seq+=1

                max_seq = max(seq, max_seq)

        return max_seq

                


        
