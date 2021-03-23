from pip._vendor.msgpack.fallback import xrange


# Use Manacher's algorithm https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
# lps - Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        text_len = len(s)
        if text_len < 2:
            return s
        position_count = 2 * text_len + 1
        l = [0] * position_count
        l[0] = 0
        l[1] = 1
        center_position = 1
        center_right_position = 2
        max_lps_length = 0
        max_lps_center_position = 0

        for current_right_position in xrange(2, position_count):

            current_left_position = 2 * center_position - current_right_position
            l[current_right_position] = 0
            diff = center_right_position - current_right_position
            if diff > 0:
                l[current_right_position] = min(l[current_left_position], diff)

            try:
                while ((current_right_position + l[current_right_position]) < position_count and (
                        current_right_position - l[current_right_position]) > 0) and (
                        ((current_right_position + l[current_right_position] + 1) % 2 == 0) or (
                        s[(current_right_position + l[current_right_position] + 1) // 2] ==
                        s[(current_right_position - l[current_right_position] - 1) // 2])):
                    l[current_right_position] += 1
            except Exception as e:
                pass

            if l[current_right_position] > max_lps_length:
                max_lps_length = l[current_right_position]
                max_lps_center_position = current_right_position

            if current_right_position + l[current_right_position] > center_right_position:
                center_position = current_right_position
                center_right_position = current_right_position + l[current_right_position]

        start = (max_lps_center_position - max_lps_length) // 2
        end = start + max_lps_length - 1
        return s[start:end + 1]


s = Solution()
print(s.longestPalindrome("babcbabcbaccba"))
print(s.longestPalindrome("ababat"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("ac"))
print(s.longestPalindrome("lenin"))
