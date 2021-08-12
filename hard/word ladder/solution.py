import string
from typing import List
from collections import deque


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        word_set = set(wordList)
        if self.search(q, beginWord, word_set, endWord):
            return 2
        seq = 1
        while q:
            seq += 1
            temp_q = deque()
            while q:
                cur = q.popleft()
                if self.search(temp_q, cur, word_set, endWord):
                    return seq + 1
            q = temp_q
        return 0

    def search(self, q, word, word_set, end):
        for i in range(len(word)):
            for a in string.ascii_lowercase:
                t = word[:i] + a + word[i + 1:]
                if t in word_set:
                    if end == t:
                        return True
                    q.append(t)
                    word_set.remove(t)
        return False


s = Solution()
print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(s.ladderLength("a", "c", ["a", "b", "c"]))
print(s.ladderLength("hot", "dog", ["hot", "dog", "dot"]))
print(s.ladderLength("hot", "dog", ["hot", "dog"]))
print(s.ladderLength("hot", "dog", ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]))
print(s.ladderLength("hit", "cog", ["hot", "cog", "dot", "dog", "hit", "lot", "log"]))
print(s.ladderLength("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]))
