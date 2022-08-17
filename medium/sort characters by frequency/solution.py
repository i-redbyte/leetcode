import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        result = ''
        l = sorted(list(set(s)), key=s.count, reverse=True)
        for i in l:
            result += i * s.count(i)
        return result

    def frequencySort1(self, s: str) -> str:
        return "".join(char * times for char, times in collections.Counter(s).most_common())


print(Solution().frequencySort("tree"))
print(Solution().frequencySort("cccaaa"))
print(Solution().frequencySort("Aabb"))
