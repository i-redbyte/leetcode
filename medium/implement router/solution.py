from collections import deque
from bisect import bisect_left, bisect_right
from typing import List


class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.q = deque()  # FIFO: (s, d, t)
        self.seen = set()  # {(s, d, t)}
        self.times = {}  # d -> List[int] (non-decreasing)
        self.offset = {}  # d -> int (first valid index in times[d])

    def _evict_oldest(self) -> None:
        if not self.q:
            return
        s, d, t = self.q.popleft()
        self.seen.remove((s, d, t))
        off = self.offset.get(d, 0)
        if self.times[d][off] == t:
            off += 1
            self.offset[d] = off
        else:
            i = bisect_left(self.times[d], t, lo=off)
            self.offset[d] = i + 1

        if self.offset[d] >= 1024 and self.offset[d] * 2 >= len(self.times[d]):
            self.times[d] = self.times[d][self.offset[d]:]
            self.offset[d] = 0

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False

        if len(self.q) >= self.limit:
            self._evict_oldest()

        self.q.append(key)
        self.seen.add(key)

        if destination not in self.times:
            self.times[destination] = []
            self.offset[destination] = 0
        self.times[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        s, d, t = self.q[0]
        self._evict_oldest()
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ts = self.times.get(destination)
        if not ts:
            return 0
        lo = self.offset.get(destination, 0)
        L = bisect_left(ts, startTime, lo=lo)
        R = bisect_right(ts, endTime, lo=lo)
        return R - L
