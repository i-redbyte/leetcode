from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combine = zip(heights, names)
        result = []
        c = sorted(combine, reverse=True)
        for _, j in c:
            result.append(j)
        return result

    def sortPeople1(self, names: List[str], heights: List[int]) -> List[str]:
        def quickSort(l: int, r: int):
            i, j = l, r
            x = heights[(l + r) // 2]
            while True:
                while heights[i] > x:
                    i += 1
                while heights[j] < x:
                    j -= 1
                if i <= j:
                    tmp = heights[i]
                    heights[i] = heights[j]
                    heights[j] = tmp
                    tmp = names[i]
                    names[i] = names[j]
                    names[j] = tmp

                    i += 1
                    j -= 1
                if i > j:
                    break
            if l < j:
                quickSort(l, j)
            if i < r:
                quickSort(i, r)

        n = len(heights) - 1
        quickSort(0, n)
        return names


s = Solution()
print(s.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
print(s.sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150]))
