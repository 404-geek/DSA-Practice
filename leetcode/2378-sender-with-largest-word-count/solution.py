class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:

        r = len(messages)
        map = defaultdict(int)
        heap = []

        for i in range(r):

            a = messages[i]
            b = senders[i]

            map[b] += len(a.split())

        ans = None

        print(map)

        for a, b in map.items():

            if ans is None or b > map[ans] or (b == map[ans] and a > ans):
                ans = a

        return ans




        
