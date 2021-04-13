# Buddy Strings #

Given two strings a and b, return true if you can swap two letters in a so the result is equal to b, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at a[i] and a[j].
- For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:
```
Input: a = "ab", b = "ba"
Output: true
Explanation: You can swap a[0] = 'a' and a[1] = 'b' to get "ba", which is equal to b.
```

Example 2:
```
Input: a = "ab", b = "ab"
Output: false
Explanation: The only letters you can swap are a[0] = 'a' and a[1] = 'b', which results in "ba" != b.
```

Example 3:
```
Input: a = "aa", b = "aa"
Output: true
Explanation: You can swap a[0] = 'a' and a[1] = 'a' to get "aa", which is equal to b.
```

Example 4:
```
Input: a = "aaaaaaabc", b = "aaaaaaacb"
Output: true
```

Constraints:

- 1 <= a.length, b.length <= 2 * 10^4
- a and b consist of lowercase letters.

[Links](https://leetcode.com/problems/buddy-strings/)