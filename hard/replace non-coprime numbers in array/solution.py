from math import gcd
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st: List[int] = []
        for x in nums:
            cur = x
            while st:
                g = gcd(st[-1], cur)
                if g == 1:
                    break
                cur = (st.pop() // g) * cur
            st.append(cur)
        return st


s = Solution()
print(s.replaceNonCoprimes(nums=[6, 4, 3, 2, 7, 6, 2]))
print(s.replaceNonCoprimes(nums=[2, 2, 1, 1, 3, 3, 3]))
