from collections import defaultdict
from typing import List


class Solution:
    def find_emails(self, email, connections, visited, account):
        if email in visited:
            return
        visited.add(email)
        account.append(email)
        for connectedEmail in connections[email]:
            self.find_emails(connectedEmail, connections, visited, account)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        merged_accounts = []
        visited = set()
        connections = defaultdict(list)

        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                if email == first_email:
                    continue
                connections[email].append(first_email)
                connections[first_email].append(email)

        for account in accounts:
            if account[1] in visited:
                continue
            merged_account = [account[0]]
            self.find_emails(account[1], connections, visited, merged_account)
            merged_account[1:] = sorted(merged_account[1:])
            merged_accounts.append(merged_account)

        return merged_accounts


s = Solution()
print(s.accountsMerge(
    [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
     ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]))

print(s.accountsMerge(
    [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
     ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
     ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]))
