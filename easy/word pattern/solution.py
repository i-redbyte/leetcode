class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        words_dic = {}
        pattern_dic = {}
        for i, v in enumerate(pattern):
            if (v in words_dic) and words_dic[v] != words[i]:
                return False
            elif (words[i] in pattern_dic) and pattern_dic[words[i]] != v:
                return False
            words_dic[v] = words[i]
            pattern_dic[words[i]] = v
        return True


s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog cat cat fish"))
print(s.wordPattern("aaaa", "dog cat cat dog"))
print(s.wordPattern("abba", "dog dog dog dog"))
