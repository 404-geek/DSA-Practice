class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        arr = []

        for s in strs:
            res[''.join(sorted(s))].append(s)

        return list(res.values())
        
