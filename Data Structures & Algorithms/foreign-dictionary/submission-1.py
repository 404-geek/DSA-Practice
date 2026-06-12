class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        n = len(words)
        adj = {c : set() for word in words for c in word}

        for i in range(n-1):

            w1, w2 = words[i], words[i+1]
            min_l = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_l] == w2[:min_l]:
                return ""

            for j in range(min_l):

                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        res = []
        vis = {}

        def dfs(char):

            if char in vis:
                return vis[char]

            vis[char] = False

            for nei in adj[char]:
                if not dfs(nei):
                    return False

            vis[char] = True
            res.append(char)

            return True

        for char in adj:
            if not dfs(char):
                return ""

        res.reverse()
        return "".join(res)
        
