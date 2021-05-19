# Binary Prefix Divisible By 5 #

Given an array nums of 0s and 1s, consider xi: the i-th subarray from nums[0] to nums[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if xi is divisible by 5.

Example 1:
```
Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: 
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
```

Example 2:
```
Input: nums = [1,1,1]
Output: [false,false,false]
```

Example 3:
```
Input: nums = [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]
```

Example 4:
```
Input: nums = [1,1,1,0,1]
Output: [false,false,false,false,false]
```

Note:

- 1 <= nums.length <= 30000
- nums[i] is 0 or 1

[Link](https://leetcode.com/problems/binary-prefix-divisible-by-5/)