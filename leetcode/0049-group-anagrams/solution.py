class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            a = [0] * 26

            for ch in s:

                a[ord(ch) - ord('a')]+=1

            res[tuple(a)].append(s)

        return list(res.values())

                




            
