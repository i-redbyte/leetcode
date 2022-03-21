from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        symbol_last_pos = {ch: i for i, ch in enumerate(s)}
        k = 0
        marker = 0
        result = []
        for i, c in enumerate(s):
            k = max(k, symbol_last_pos[c])
            if i == k:
                result.append(i - marker + 1)
                marker = i + 1
        return result


s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
print(s.partitionLabels("eccbbbbdec"))
