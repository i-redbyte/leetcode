import collections
import copy
from typing import List


class Solution:
    def get_value_count(self, w_d, counter, score):
        val = 0
        local_counter = copy.deepcopy(counter)
        for w in w_d:
            x = 0
            for v in w:
                if local_counter.get(v, 0) > 0:
                    local_counter[v] -= 1
                    x += score[ord(v) - ord('a')]
                else:
                    x = 0
                    break
            val += x
        return val

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        result = 0
        counter = collections.Counter(letters)
        n = len(words)
        for mask in range(1 << n):
            w = []
            for i in range(n):
                if mask & (1 << i):
                    w.append(words[i])
            result = max(result, self.get_value_count(w, counter, score))
        return result


print(
    Solution().maxScoreWords(words=["dog", "cat", "dad", "good"], letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                             score=[1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(Solution().maxScoreWords(words=["xxxz", "ax", "bx", "cx"], letters=["z", "a", "b", "c", "x", "x", "x"],
                               score=[4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]))
print(Solution().maxScoreWords(words=["leetcode"], letters=["l", "e", "t", "c", "o", "d"],
                               score=[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]))
