class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) >= len(b):
            a, b = a, "0" * (len(a) - len(b)) + b
        else:
            a, b = "0" * (len(b) - len(a)) + a, b
        c = 0
        result = ""
        for i in range(len(a) - 1, -1, -1):
            if (a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0"):
                if c == 0:
                    result = "1" + result
                    c = 0
                else:
                    result = "0" + result
                    c = 1
            else:
                result = "0" + result if c == 0 else "1" + result
                if a[i] == "1":
                    c = 1
                else:
                    c = 0
        if c == 1:
            return "1" + result
        return result


s = Solution()
print(s.addBinary("11", "1"))
print(s.addBinary("1010", "1011"))
print(s.addBinary("0", "0"))
