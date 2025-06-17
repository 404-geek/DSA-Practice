class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        res = []

        groups = defaultdict(list)
        
        for i, ele in enumerate(groupSizes):

            groups[ele].append(i)

            if len(groups[ele]) == ele:
                res.append(groups[ele])
                groups[ele] = []

        return res

