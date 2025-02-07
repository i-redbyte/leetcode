from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_color = {}
        color_count = {}
        result = []

        for x, y in queries:

            if x in ball_to_color:
                old_color = ball_to_color[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]

            ball_to_color[x] = y
            color_count[y] = color_count.get(y, 0) + 1

            result.append(len(color_count))

        return result


s = Solution()
print(s.queryResults(limit=4, queries=[[1, 4], [2, 5], [1, 3], [3, 4]]))
print(s.queryResults(limit=4, queries=[[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]))
