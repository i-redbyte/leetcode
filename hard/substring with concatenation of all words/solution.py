import collections
import copy
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not words[0]:
            return None
        counter = collections.defaultdict(int)
        len_word = len(words[0])
        target_len = len(words) * len_word
        for word in words:
            counter[word] += 1
        result = []
        for i in range(len_word):
            count = copy.copy(counter)
            pos = i
            n = len(s)
            while pos < n - len_word + 1:
                count[s[pos:pos + len_word]] -= 1
                while count[s[pos:pos + len_word]] < 0:
                    count[s[i:i + len_word]] += 1
                    i += len_word
                pos += len_word
                if pos - i == target_len: result.append(i)
        return result


s = Solution()
print(s.findSubstring("barfoothefoobarman", words=["foo", "bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))
print(s.findSubstring("barfoofoobarthefoobarman", words=["bar", "foo", "the"]))
