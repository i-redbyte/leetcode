from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank:
            return -1
        len_bank_item = len(bank[0])
        bank = set(bank)
        if end not in bank:
            return -1
        q = deque()
        q.append((start, 0))
        seen = set()
        while q:
            gene, height = q.popleft()
            for i in range(len_bank_item):
                for char in {'A', 'C', 'G', 'T'} - {gene[i]}:
                    new_gene = gene[:i] + char + gene[i + 1:]
                    if new_gene == end:
                        return height + 1
                    if new_gene in bank and new_gene not in seen:
                        q.append((new_gene, height + 1))
                        seen.add(new_gene)
        return -1


s = Solution()

print(s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
print(s.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
print(s.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]))
