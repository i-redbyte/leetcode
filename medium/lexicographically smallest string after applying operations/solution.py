from math import gcd


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s = list(map(int, s))
        n = len(s)
        step = gcd(b, n)
        g = gcd(a, 10)
        result = [10]

        def modify(start: int) -> None:
            ch = t[start]
            inc = ch % g - ch
            if inc:
                for j in range(start, n, 2):
                    t[j] = (t[j] + inc) % 10

        for i in range(0, n, step):
            t = s[i:] + s[:i]
            modify(1)
            if step % 2:
                modify(0)
            result = min(result, t)

        return ''.join(map(str, result))

    def findLexSmallestString1(self, s: str, a: int, b: int) -> str:
        n = len(s)
        a %= 10
        t = 10 // gcd(a, 10) if a else 1

        shifts_left = []
        seen = set()
        r = 0
        for _ in range(n):
            if r in seen:
                break
            seen.add(r)
            shifts_left.append((n - r) % n)
            r = (r + b) % n

        rotated_list = [s[sh:] + s[:sh] for sh in shifts_left]

        def apply_add(st: str, k_even: int, k_odd: int) -> str:
            add_e = (k_even * a) % 10
            add_o = (k_odd * a) % 10
            out = []
            for i, ch in enumerate(st):
                d = ord(ch) - 48
                d = (d + (add_o if (i & 1) else add_e)) % 10
                out.append(chr(48 + d))
            return ''.join(out)

        result = s
        if b % 2 == 0:
            for k_odd in range(t):
                for rot in rotated_list:
                    cand = apply_add(rot, 0, k_odd)
                    if cand < result:
                        result = cand
        else:
            for k_odd in range(t):
                for k_even in range(t):
                    for rot in rotated_list:
                        cand = apply_add(rot, k_even, k_odd)
                        if cand < result:
                            result = cand
        return result


s = Solution()

print(s.findLexSmallestString(s="5525", a=9, b=2))
print(s.findLexSmallestString(s="74", a=5, b=1))
print(s.findLexSmallestString(s="0011", a=4, b=2))
