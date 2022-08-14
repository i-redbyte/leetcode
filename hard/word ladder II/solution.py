import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        nowhere = collections.defaultdict(list)
        wordList.append(beginWord)
        result = []
        attitude = {beginWord}
        queue = collections.deque([(beginWord, [beginWord])])
        for w in wordList:
            n = len(w)
            for j in range(n):
                pattern = w[:j] + '±' + w[j + 1:]
                nowhere[pattern].append(w)
        while queue:
            tmp = set()
            n = len(queue)
            for i in range(n):
                w, s = queue.popleft()
                if w == endWord:
                    result.append(s)
                m = len(w)
                for j in range(m):
                    pattern = w[:j] + '±' + w[j + 1:]
                    for a in nowhere[pattern]:
                        if a not in attitude:
                            queue.append((a, s[:] + [a]))
                            tmp.add(a)
            attitude.update(tmp)
        return result


s = Solution()
print(s.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(s.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))
