class Solution:
    def is_uint(self, st):
        if st == "":
            return False
        return set(st).issubset("0123456789")

    def is_int(self, st):
        if st == "":
            return False
        if st[0] in "+-":
            return self.is_uint(st[1:])
        return self.is_uint(st)

    def is_decimal(self, st):
        if st == "":
            return False
        for c, ss in enumerate(st):
            if ss == ".":
                break
        else:
            return self.is_int(st)
        left = st[:c]
        right = st[c + 1:]
        return (((left in "+-") and self.is_uint(right)) or
                (self.is_int(left) and (self.is_uint(right) or right == "")))

    def isNumber(self, s: str) -> bool:
        for c, ss in enumerate(s):
            if ss in "eE":
                break
        else:
            return self.is_decimal(s) or self.is_int(s)
        return self.is_decimal(s[:c]) & self.is_int(s[c + 1:])

s = Solution()
print(s.isNumber("0"))
print(s.isNumber("e"))
print(s.isNumber("."))
