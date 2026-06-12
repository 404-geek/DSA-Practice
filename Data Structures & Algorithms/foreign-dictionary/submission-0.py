class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        n = len(words)
        adj = {c : set() for word in words for c in word}

        indegree = {c : 0 for c in adj}

        for i in range(n-1):

            w1, w2 = words[i], words[i+1]
            min_l = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_l] == w2[:min_l]:
                return ""

            for j in range(min_l):

                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1

                    break

        q = deque([c for c in indegree if indegree[c] == 0])

        res = []

        while q:
            c = q.popleft()
            res.append(c)
            
            for nei in adj[c]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    q.append(nei)
            
        
        if len(res) != len(indegree):
            return ""

        return "".join(res)
         

 