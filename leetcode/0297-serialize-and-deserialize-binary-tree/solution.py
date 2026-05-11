# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        res = []

        q = deque([root])

        while q:

            n = q.popleft()

            if n:
                res.append(str(n.val))
                q.append((n.left))
                q.append((n.right))
            else:
                res.append('#')

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(",")
        r = data[0]
        root = TreeNode(r)
        q = deque([root])
        i = 1

        while q:

            for _ in range(len(q)):

                n = q.popleft()

                l = data[i]
                r = data[i+1]

                if l == "#":
                    n.left = None
                else:
                    new_node_l = TreeNode(l)
                    n.left = new_node_l
                    q.append((new_node_l))

                if r == "#":
                    n.right = None
                else:
                    new_node_r = TreeNode(r)
                    n.right = new_node_r
                    q.append((new_node_r))

                i+=2

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
