class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result_string = ""
        start_pos = 0
        m = {}
        i = 0
        for c in s:
            if c in m:
                start_pos = max(m[c] + 1, start_pos)
            if len(result_string) < i - start_pos + 1:
                result_string = s[start_pos: i + 1]
            m[c] = i
            i += 1
        return len(result_string)


# Test:
s = Solution()
print(s.lengthOfLongestSubstring("abaxrtcabdgtgg"))
print(s.lengthOfLongestSubstring("assembler"))
print(s.lengthOfLongestSubstring("lll"))
print(s.lengthOfLongestSubstring(""))
