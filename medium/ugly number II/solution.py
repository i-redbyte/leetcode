class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [1]
        u2_idx, u3_idx, u5_idx = 0, 0, 0
        while len(ugly_nums) < n:
            u2_num = ugly_nums[u2_idx] * 2
            u3_num = ugly_nums[u3_idx] * 3
            u5_num = ugly_nums[u5_idx] * 5
            cur_ugly = min(min(u2_num, u3_num), u5_num)
            if cur_ugly == u2_num:
                u2_idx += 1
            if cur_ugly == u3_num:
                u3_idx += 1
            if cur_ugly == u5_num:
                u5_idx += 1
            ugly_nums.append(cur_ugly)
        return ugly_nums[n-1]


s = Solution()
print(s.nthUglyNumber(10))
print(s.nthUglyNumber(1))
