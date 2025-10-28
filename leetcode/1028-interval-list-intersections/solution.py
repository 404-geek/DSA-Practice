class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
         
        start, end = 0,0
        res = []

        while start < len(firstList) and end < len(secondList):

            a = max(firstList[start][0], secondList[end][0])
            b = min(firstList[start][1], secondList[end][1])

            if a <= b:

                res.append([a,b])

            if firstList[start][1] < secondList[end][1]:
                start+=1
            else:
                end+=1
        
        return res
