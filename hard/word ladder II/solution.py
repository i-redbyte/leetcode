import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        result = []
        d = collections.defaultdict(list)
        for w in wordList:
            n = len(w)
            for i in range(n):
                d[w[:i] + "±" + w[i + 1:]].append(w)

        if endWord not in wordList:
            return []

        visiter1 = collections.defaultdict(list)
        queue1 = collections.deque([beginWord])
        visiter1[beginWord] = []
        visiter2 = collections.defaultdict(list)
        queue2 = collections.deque([endWord])
        visiter2[endWord] = []

        def dfs(k, visiter, path, paths):
            path.append(k)
            if not visiter[k]:
                if visiter is visiter1:
                    paths.append(path[::-1])
                else:
                    paths.append(path[:])
            for i in visiter[k]:
                dfs(i, visiter, path, paths)
            path.pop()

        def bfs(queue, visited1, visited2, startBegin):
            level = collections.defaultdict(list)
            for _ in range(len(queue)):
                l = queue.popleft()
                n = len(l)
                for i in range(n):
                    for j in d[l[:i] + "±" + l[i + 1:]]:
                        if j in visited2:
                            paths1 = []
                            paths2 = []
                            dfs(l, visited1, [], paths1)
                            dfs(j, visited2, [], paths2)
                            if not startBegin:
                                paths1, paths2 = paths2, paths1
                            for a in paths1:
                                for b in paths2:
                                    result.append(a + b)
                        elif j not in visited1:
                            if j not in level:
                                queue.append(j)
                            level[j].append(l)
            visited1.update(level)

        while queue1 and queue2 and not result:
            n = len(queue1)
            m = len(queue2)
            if n > m:
                bfs(queue2, visiter2, visiter1, False)
            else:
                bfs(queue1, visiter1, visiter2, True)
        return result

    def findLadders1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
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
