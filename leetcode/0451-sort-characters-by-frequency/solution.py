class Solution:
    def frequencySort(self, s: str) -> str:
        map = defaultdict(int)
        for i in s:

            map[i]+=1

        map = sorted(map.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for b in map:
            ans.append(b[1] * b[0])

        return "".join(ans)



        
