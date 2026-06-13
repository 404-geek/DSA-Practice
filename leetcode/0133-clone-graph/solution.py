"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        vis = {}

        def dfs(node):

            if node in vis:
                return vis[node]

            new_node = Node(node.val)
            vis[node] = new_node

            for no in node.neighbors:
                new_node.neighbors.append(dfs(no))

            return new_node

        return dfs(node)

