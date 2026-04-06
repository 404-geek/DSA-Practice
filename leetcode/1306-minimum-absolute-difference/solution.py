class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr = sorted(arr)

        res = [[arr[0],arr[1]]]
        min_diff = arr[1] - arr[0]

        for i in range(1, len(arr)-1):

            t = arr[i+1] - arr[i]

            if t == min_diff:
                res.append([arr[i], arr[i+1]])

            elif t < min_diff:
                min_diff = t
                res = [[arr[i], arr[i+1]]]


        return res
            




