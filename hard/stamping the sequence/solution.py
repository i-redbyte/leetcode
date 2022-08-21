from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        result = []
        s = set()
        n = len(stamp)
        target_length = len(target)
        complete = '?' * target_length
        for i in range(n):
            for j in range(n - i):
                s.add('?' * i + stamp[i:n - j] + '?' * j)
        m = target_length - n
        while target != complete:
            is_find = False
            for i in range(m, -1, -1):
                if target[i: i + n] in s:
                    target = target[:i] + '?' * n + target[i + n:]
                    result.append(i)
                    is_find = True
            if not is_find:
                return []

        return result[::-1]


print(Solution().movesToStamp(stamp="abc", target="ababc"))
print(Solution().movesToStamp(stamp="abca", target="aabcaca"))
