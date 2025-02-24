from collections import defaultdict
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        time_bob = [-1] * n

        def find_bob_path(node, parent, time):
            if node == 0:
                time_bob[node] = time
                return True
            for neighbor in tree[node]:
                if neighbor != parent:
                    if find_bob_path(neighbor, node, time + 1):
                        time_bob[node] = time
                        return True
            return False

        def dfs(node, parent, t, current_profit):
            nonlocal max_profit

            if time_bob[node] == -1 or t < time_bob[node]:
                current_profit += amount[node]
            elif t == time_bob[node]:
                current_profit += amount[node] // 2
            else:
                current_profit += 0

            is_leaf = len(tree[node]) == 1 and node != 0
            if is_leaf:
                max_profit = max(max_profit, current_profit)

            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs(neighbor, node, t + 1, current_profit)

        find_bob_path(bob, -1, 0)
        max_profit = float('-inf')
        dfs(0, -1, 0, 0)
        return int(max_profit)


s = Solution()
print(s.mostProfitablePath(edges=[[0, 1], [1, 2], [1, 3], [3, 4]], bob=3, amount=[-2, 4, 2, -4, 6]))
print(s.mostProfitablePath(edges=[[0, 1]], bob=1, amount=[-7280, 2350]))
