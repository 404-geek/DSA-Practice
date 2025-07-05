class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        temp = sorted(arr)
        min_diff = float('inf')
        res = []

    
        for i in range(1, len(temp)):
            diff = temp[i] - temp[i - 1]
            if diff < min_diff:
                min_diff = diff

    
        for i in range(1, len(temp)):
            if temp[i] - temp[i - 1] == min_diff:
                res.append([temp[i - 1], temp[i]])

        return res


