class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        uppers, lowers, digits = 0, 0, 0
        for c in password:
            if not uppers and c.isupper():
                uppers = 1
            if not lowers and c.islower():
                lowers = 1
            if not digits and c.isdigit():
                digits = 1

        swaps = (3 - (uppers + lowers + digits))

        i, j = 0, 1
        eq = list()
        while i < n:
            while j < n and password[i] == password[j]:
                j += 1
            eq.append(j-i)
            i, j = j, j+1

        if n < 6:
            adds = 6 - n
            return max(adds, swaps)
        elif n <= 20:
            r_swaps = sum([elem // 3 for elem in eq])
            return max(swaps, r_swaps)
        else:
            subs = n - 20
            r = len(eq)
            for i in range(r):
                if subs >= 1 and eq[i] % 3 == 0:
                    eq[i] -= 1
                    subs -= 1
            for i in range(r):
                if subs >= 2 and eq[i] % 3 == 1 and eq[i] > 3:
                    eq[i] -= 2
                    subs -= 2
            for i in range(r):
                if subs > 0 and eq[i] > 2:
                    removed = min(subs, eq[i] - 2)
                    eq[i] -= removed
                    subs -= removed

            r_swaps = sum([elem // 3 for elem in eq])
            return max(swaps, r_swaps) + (n - 20)


s = Solution()
print(s.strongPasswordChecker("a"))
print(s.strongPasswordChecker("aA1"))
print(s.strongPasswordChecker("1337C0d3"))
