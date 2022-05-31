class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        need = 1 << k
        got = [False]*need
        all_one = need - 1
        hash = 0
        for i in range(n):
            hash = ((hash << 1) & all_one) | (int(s[i]))
            if i >= k-1 and got[hash] is False:
                got[hash] = True
                need -= 1
                if need == 0:
                    return True
        return False


s = Solution()
print(s.hasAllCodes(s="00110110", k=2))
print(s.hasAllCodes(s="0110", k=1))
print(s.hasAllCodes(s="0110", k=2))
