from typing import List, Tuple, Dict
import heapq


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task: Dict[int, Tuple[int, int]] = {}
        self.h: List[Tuple[int, int, int]] = []

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task[taskId] = (userId, priority)
        heapq.heappush(self.h, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task[taskId]
        self.task[taskId] = (userId, newPriority)
        heapq.heappush(self.h, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task:
            del self.task[taskId]

    def execTop(self) -> int:
        while self.h:
            negP, negId, taskId = heapq.heappop(self.h)
            if taskId not in self.task:
                continue
            userId, curP = self.task[taskId]
            if -negP == curP:
                del self.task[taskId]
                return userId
        return -1
