class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = defaultdict(set)

        for word in words:
            for ch in word:
                adj[ch]

        for a in range(1, len(words)):

            w1 = words[a-1]
            w2 = words[a]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for ch1,ch2 in zip(w1,w2):

                if ch1 != ch2:
                    adj[ch1].add(ch2)
                    break

        print(adj)

        vis = {}
        res = []
        
        def dfs(node):
                
            if node in vis and vis[node] == 1:
                return False

            if node in vis and vis[node] == 2:
                return True
            
            vis[node] = 1

            if node in adj:

                for ch in adj[node]:

                    if not dfs(ch):
                        return False

            res.append(node)

            vis[node] = 2

            return True

        for ch in adj:
            if not dfs(ch):
                return ""
        
        return "".join(reversed(res))

            




            
        