from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            if x not in parent:
                parent[x] = x

            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                parent[root_y] = root_x

        # 1. Union emails inside same account
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                email_to_name[email] = name
                union(first_email, email)

        # 2. Group emails by root parent
        groups = defaultdict(list)

        for email in email_to_name:
            root = find(email)
            groups[root].append(email)

        # 3. Build result
        res = []

        for root, emails in groups.items():
            name = email_to_name[root]
            res.append([name] + sorted(emails))

        return res
    
accounts = [
    ["John", "a@gmail.com", "b@gmail.com"],
    ["John", "b@gmail.com", "c@gmail.com"],
    ["Mary", "d@gmail.com"]
]

sol = Solution()

result = sol.accountsMerge(accounts)

print(result)