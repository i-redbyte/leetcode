class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        result = ""
        d = {}
        x = 0
        for c in key:
            if c != ' ' and c not in d:
                d[c] = chr(97 + x)
                x += 1
        for c in message:
            if c == ' ':
                result += ' '
            else:
                result += d[c]
        return result


s = Solution()

print(s.decodeMessage(key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv"))
print(s.decodeMessage(key="eljuxhpwnyrdgtqkviszcfmabo", message="zwx hnfx lqantp mnoeius ycgk vcnjrdb"))
