from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr) - 1
        q = [start]
        is_visited = [0] * len(arr)
        while len(q):
            num = q.pop(0)
            if is_visited[num] == 1:
                continue
            if arr[num] == 0:
                return True
            if num + arr[num] <= n:
                q.append(num + arr[num])
            if num - arr[num] >= 0:
                q.append(num - arr[num])
            is_visited[num] = 1
        return False


s = Solution()

print(s.canReach([4, 2, 3, 0, 3, 1, 2], 5))
print(s.canReach([4, 2, 3, 0, 3, 1, 2], 0))
print(s.canReach([3, 0, 2, 1, 2], 2))
