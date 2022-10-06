class Solution:
    def countArrangement(self, n: int) -> int:
        def backtracking(index: int = 1, values=None):
            if values is None:
                values = set()
            if len(values) == n:
                return 1

            total = 0
            for value in range(1, n + 1):
                if value in values:
                    continue
                if index % value == 0 or value % index == 0:
                    values.add(value)
                    total += backtracking(index + 1, values)
                    values.remove(value)
            return total

        return backtracking()


s = Solution()
print(s.countArrangement(2))
print(s.countArrangement(1))
