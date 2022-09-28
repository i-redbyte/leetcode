from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        result = []
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in dic:
                dic[sortedWord] = [word]
            else:
                dic[sortedWord].append(word)
        for value in dic.values():
            result.append(value)
        return result


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
