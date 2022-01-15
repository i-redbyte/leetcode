from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]
        curs = set([0])
        counter_v = {0, n-1}
        step = 0
        tmp = set([n-1])
        while curs:
            if len(curs) > len(tmp):
                curs, tmp = tmp, curs
            nex = set()
            for node in curs:
                for child in graph[arr[node]]:
                    if child in tmp:
                        return step + 1
                    if child not in counter_v:
                        counter_v.add(child)
                        nex.add(child)

                graph[arr[node]].clear()

                for child in [node-1, node+1]:
                    if child in tmp:
                        return step + 1
                    if 0 <= child < len(arr) and child not in counter_v:
                        counter_v.add(child)
                        nex.add(child)
            curs = nex
            step += 1
        return -1

s = Solution()
print(s.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
print(s.minJumps([7]))
print(s.minJumps([7,6,9,6,9,6,9,7]))