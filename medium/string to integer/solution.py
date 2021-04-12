class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        start_position = 0
        while start_position < n and s[start_position] == ' ':
            start_position += 1

        if len(s[start_position:]) == 0:
            return 0

        negative = False
        if s[start_position] in ('-', '+'):
            negative = s[start_position] == '-'
            start_position += 1

        result = 0
        while start_position < n and ord('0') <= ord(s[start_position]) <= ord('9'):
            result = (result << 1) + (result << 3) + ord(s[start_position]) - ord('0')

            if negative and result > 2147483648:
                return -2147483648

            if not negative and result > 2147483647:
                return 2147483647

            start_position += 1
        if negative:
            return (~result) + 1
        else:
            return result


s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi("    -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("-91283472332"))
print(s.myAtoi("-1 2 3"))
