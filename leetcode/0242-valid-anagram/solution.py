class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        st = Counter(s)
        tt = Counter(t)

        longest, shortest = (st, tt) if len(st) >= len(tt) else (tt, st)

        for key, val in longest.items():
            if longest.get(key) != shortest.get(key):
                return False
        
        return True

        
