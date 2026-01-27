from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        OFFSET = 10000
        MAX = 20000

        max_end = [-1] * (MAX + 1)

        min_s = MAX
        max_e = 0

        for s, e in intervals:
            si = s + OFFSET
            ei = e + OFFSET
            if ei > max_end[si]:
                max_end[si] = ei
            if si < min_s:
                min_s = si
            if ei > max_e:
                max_e = ei

        merged: List[List[int]] = []
        append = merged.append

        i = min_s
        while i <= max_e:
            if max_end[i] == -1:
                i += 1
                continue

            start = i
            end = max_end[i]
            i += 1

            while i <= end and i <= max_e:
                ei = max_end[i]
                if ei > end:
                    end = ei
                i += 1

            append([start - OFFSET, end - OFFSET])

        return merged

    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
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
