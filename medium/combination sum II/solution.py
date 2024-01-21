from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]) -> List[int]:
            if target == 0:
                result.append(list(path))
                return
            if target < 0:
                return

            previous = -1
            for i in range(start, len(candidates)):
                if candidates[i] == previous:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
                previous = candidates[i]

        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result

    def combinationSum2_1(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]) -> List[int]:
            if target == 0:
                result.append(path)
                return []
            if target < 0:
                return []

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result


s = Solution()
print(s.combinationSum2_1(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
print(s.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
