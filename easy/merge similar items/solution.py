from collections import Counter
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        return sorted((Counter({i[0]: i[1] for i in items1}) + Counter({i[0]: i[1] for i in items2})).items())


print(Solution().mergeSimilarItems([[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]))
print(Solution().mergeSimilarItems([[1, 1], [3, 2], [2, 3]], items2=[[2, 1], [3, 2], [1, 3]]))
print(Solution().mergeSimilarItems(items1=[[1, 3], [2, 2]], items2=[[7, 1], [2, 2], [1, 4]]))
