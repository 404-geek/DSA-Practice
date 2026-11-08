class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        adj = defaultdict(list)
        

        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        
        n = len(tickets)


        out = []

        def dfs(airport):

            while adj[airport]:

                next = adj[airport].pop()
                dfs(next)

            out.append(airport)

        dfs("JFK")
        
        return out[::-1]


        
