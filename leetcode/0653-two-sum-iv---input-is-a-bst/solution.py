# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        stack_next = []
        stack_before = []

        a = root

        while root:
            stack_next.append(root)
            root = root.left

        root = a

        while root:
            stack_before.append(root)
            root = root.right

        def get_next():

            if not stack_next:
                return None

            a = stack_next.pop()

            root = a.right

            while root:
                stack_next.append(root)
                root = root.left
            
            return a.val

        def get_before():

            if not stack_before:
                return None

            a = stack_before.pop()

            root = a.left

            while root:
                stack_before.append(root)
                root = root.right

            return a.val

        i = get_next()
        j = get_before()

        while i < j:

            su = i + j

            if su == k:
                return True
            elif su > k:
                j = get_before()
            else:
                i = get_next()


        return False
             

