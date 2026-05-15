class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        m_cnt = 0
        cnt = 0

        for n in nums:

            if n == 1:
                cnt += 1
            else:
                cnt = 0
                
            m_cnt = max(cnt, m_cnt)

        return m_cnt
        
