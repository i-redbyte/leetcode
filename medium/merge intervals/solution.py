from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: (x[0], x[1]))

        result: List[List[int]] = []
        cur_start, cur_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= cur_end:
                cur_end = max(cur_end, end)
            else:
                result.append([cur_start, cur_end])
                cur_start, cur_end = start, end

        result.append([cur_start, cur_end])
        return result


s = Solution()

print(s.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge(intervals=[[1, 4], [4, 5]]))
print(s.merge(intervals=[[4, 7], [1, 4]]))
