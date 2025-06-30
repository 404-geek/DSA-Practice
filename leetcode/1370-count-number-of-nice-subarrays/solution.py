class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):

            if nums[i] % 2 != 0:
                nums[i] = 1
        
        pref_freq = defaultdict(int)
        pref_freq[0] = 1
        res = 0
        odd_count = 0

        for j in nums:


            if j == 1:
                odd_count += 1

            res += pref_freq[odd_count - k]
            pref_freq[odd_count] += 1

            
        return res




