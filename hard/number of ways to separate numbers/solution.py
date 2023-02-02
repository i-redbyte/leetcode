class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        counts = [[0] * (n + 1) for _ in range(n)]
        all_same_flag = True if num.count(num[0]) == len(num) else False
        for i in range(n):
            counts[i][n] = 1 if num[i] != '0' else 0

        def compare(i, j) -> int:
            if i == j or all_same_flag:
                return 0
            elif num[i] != num[j]:
                return i + 1 if num[i] > num[j] else -(i + 1)
            elif 2 * j - i == n or 2 * j - i == n - 1:
                for k in range(j - i):
                    if num[i + k] != num[j + k]:
                        return i + k if num[i + k] > num[j + k] else -(i + k + 1)
                return 0
            else:
                idx = compare(i + 1, j + 1)
                return 0 if idx == 0 or abs(idx) - 1 >= j else idx

        result = counts[0][n]
        for j in range(n - 1, 0, -1):
            k, total = n, 0
            for i in range(j):
                if num[i] != '0':
                    while k - j > j - i or (k - j == j - i and compare(i, j) <= 0):
                        total = (total + counts[j][k]) % int(1e9 + 7)
                        k -= 1
                    counts[i][j] = total
            result = (result + counts[0][j]) % int(1e9 + 7)
            del counts[j]
        return result


s = Solution()
print(s.numberOfCombinations("327"))
print(s.numberOfCombinations("094"))
print(s.numberOfCombinations("0"))
