from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if k > n:
            return []

        cnt = defaultdict(int)
        where = {}

        big = []
        small = []

        sum_big = 0
        big_count = 0

        def get_big_min():
            """
            Самый слабый элемент в big (минимальный freq, при равенстве — меньший val).
            Удаляет все 'протухшие' элементы наверху.
            """
            nonlocal big
            while big:
                f, v = big[0]
                if where.get(v, 0) != 2 or cnt[v] != f or f == 0:
                    heapq.heappop(big)
                else:
                    return f, v
            return None

        def get_small_max():
            """
            Самый сильный элемент в small (максимальный freq, при равенстве — больший val).
            Также чистит протухшие записи.
            """
            nonlocal small
            while small:
                nf, nv = small[0]
                f, v = -nf, -nv
                if where.get(v, 0) != 1 or cnt[v] != f or f == 0:
                    heapq.heappop(small)
                else:
                    return f, v
            return None

        def rebalance():
            """
            Поддерживаем два инварианта:
            1) в big не больше x элементов (distinct значений),
            2) любой элемент в big "не хуже" любого элемента в small
               по ключу (freq desc, value desc).
            """
            nonlocal sum_big, big_count

            while big_count > x:
                bm = get_big_min()
                if bm is None:
                    break
                f, v = bm
                heapq.heappop(big)
                where[v] = 1
                sum_big -= f * v
                big_count -= 1
                heapq.heappush(small, (-f, -v))

            while True:
                sm = get_small_max()

                if big_count < x:
                    if sm is None:
                        break
                    f_s, v_s = sm
                    heapq.heappop(small)
                    where[v_s] = 2
                    sum_big += f_s * v_s
                    big_count += 1
                    heapq.heappush(big, (f_s, v_s))
                    continue

                if sm is None:
                    break
                bm = get_big_min()
                if bm is None:
                    break

                f_b, v_b = bm
                f_s, v_s = sm

                if (f_s > f_b) or (f_s == f_b and v_s > v_b):
                    heapq.heappop(small)
                    heapq.heappop(big)

                    where[v_s] = 2
                    where[v_b] = 1

                    sum_big += f_s * v_s - f_b * v_b

                    heapq.heappush(big, (f_s, v_s))
                    heapq.heappush(small, (-f_b, -v_b))
                else:
                    break

        def add_val(v: int):
            nonlocal sum_big, big_count
            old = cnt[v]
            new = old + 1
            cnt[v] = new
            w = where.get(v, 0)

            if w == 2:
                sum_big += v
                heapq.heappush(big, (new, v))
            elif w == 1:
                heapq.heappush(small, (-new, -v))
            else:
                where[v] = 1
                heapq.heappush(small, (-new, -v))

            rebalance()

        def remove_val(v: int):
            nonlocal sum_big, big_count
            old = cnt[v]
            new = old - 1
            cnt[v] = new
            w = where.get(v, 0)

            if w == 2:
                sum_big -= v
                if new > 0:
                    heapq.heappush(big, (new, v))
                else:
                    where[v] = 0
                    big_count -= 1
            elif w == 1:
                if new > 0:
                    heapq.heappush(small, (-new, -v))
                else:
                    where[v] = 0
            else:
                pass

            rebalance()

        result: List[int] = []
        for i in range(k):
            add_val(nums[i])
        result.append(sum_big)

        for i in range(k, n):
            add_val(nums[i])
            remove_val(nums[i - k])
            result.append(sum_big)

        return result


s = Solution()
print(s.findXSum(nums=[1, 1, 2, 2, 3, 4, 2, 3], k=6, x=2))
print(s.findXSum(nums=[3, 8, 7, 8, 7, 5], k=2, x=2))
