class Fancy:
    MOD = 10**9 + 7
    MAXN = 100000 + 5

    def __init__(self):
        self.n = 0
        size = 4 * self.MAXN
        self.tree = [0] * size
        self.lazy_mul = [1] * size
        self.lazy_add = [0] * size

    def _apply(self, node: int, mul: int, add: int, l: int, r: int) -> None:
        self.tree[node] = (self.tree[node] * mul + (r - l + 1) * add) % self.MOD
        self.lazy_mul[node] = (self.lazy_mul[node] * mul) % self.MOD
        self.lazy_add[node] = (self.lazy_add[node] * mul + add) % self.MOD

    def _push(self, node: int, l: int, r: int) -> None:
        if l == r:
            return
        if self.lazy_mul[node] == 1 and self.lazy_add[node] == 0:
            return

        mid = (l + r) // 2
        left = node * 2
        right = node * 2 + 1

        self._apply(left, self.lazy_mul[node], self.lazy_add[node], l, mid)
        self._apply(right, self.lazy_mul[node], self.lazy_add[node], mid + 1, r)

        self.lazy_mul[node] = 1
        self.lazy_add[node] = 0

    def _update(self, node: int, l: int, r: int, ql: int, qr: int, mul: int, add: int) -> None:
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self._apply(node, mul, add, l, r)
            return

        self._push(node, l, r)
        mid = (l + r) // 2
        self._update(node * 2, l, mid, ql, qr, mul, add)
        self._update(node * 2 + 1, mid + 1, r, ql, qr, mul, add)
        self.tree[node] = (self.tree[node * 2] + self.tree[node * 2 + 1]) % self.MOD

    def _query(self, node: int, l: int, r: int, idx: int) -> int:
        if l == r:
            return self.tree[node]

        self._push(node, l, r)
        mid = (l + r) // 2
        if idx <= mid:
            return self._query(node * 2, l, mid, idx)
        return self._query(node * 2 + 1, mid + 1, r, idx)

    def append(self, val: int) -> None:
        self._update(1, 0, self.MAXN - 1, self.n, self.n, 1, val % self.MOD)
        self.n += 1

    def addAll(self, inc: int) -> None:
        if self.n == 0:
            return
        self._update(1, 0, self.MAXN - 1, 0, self.n - 1, 1, inc % self.MOD)

    def multAll(self, m: int) -> None:
        if self.n == 0:
            return
        self._update(1, 0, self.MAXN - 1, 0, self.n - 1, m % self.MOD, 0)

    def getIndex(self, idx: int) -> int:
        if idx < 0 or idx >= self.n:
            return -1
        return self._query(1, 0, self.MAXN - 1, idx)


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
