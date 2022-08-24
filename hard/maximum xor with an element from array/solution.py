from typing import List


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums = sorted(nums)
        bin_nums = [[(x >> i) & 1 for i in range(32)][::-1] for x in nums]
        n = len(queries)
        result = [-1] * n
        queries = sorted([(queries[i][1], queries[i][0], i) for i in range(n)])
        index = 0
        tree = {}

        for limit, target, idx in queries:
            m = len(nums)
            while index < m and nums[index] <= limit:
                node = tree
                for b in bin_nums[index]:
                    if not b in node:
                        node[b] = {}
                    node = node[b]
                index += 1

            tree_len = len(tree)
            if tree_len == 0:
                continue
            xorSum = 0
            node = tree
            for b in [(target >> i) & 1 for i in range(32)][::-1]:
                if 1 - b in node:
                    xorSum = (xorSum << 1) | 1
                    node = node[1 - b]
                else:
                    xorSum = xorSum << 1
                    node = node[b]
            result[idx] = xorSum
        return result


s = Solution()
print(s.maximizeXor(nums=[0, 1, 2, 3, 4], queries=[[3, 1], [1, 3], [5, 6]]))
print(s.maximizeXor(nums=[5, 2, 4, 6, 6, 3], queries=[[12, 4], [8, 1], [6, 3]]))
