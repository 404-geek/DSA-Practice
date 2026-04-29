class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:

        grps = defaultdict(list)
        ans = [0]* (len(arr))

        for i,a in enumerate(arr):

            grps[a].append(i)

        for l in grps.values():

            pref = 0
            total = sum(l)
            cnt= len(l)

            for j, idx in enumerate(l):
                left = idx * j - pref
                right = (total - pref - idx ) - idx *(cnt - j - 1)

                ans[idx] = left + right

                pref += idx

        
        return ans



            
        
