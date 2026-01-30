from typing import List
import heapq
from collections import deque


class Solution:
    def minimumCost(
            self,
            source: str,
            target: str,
            original: List[str],
            changed: List[str],
            cost: List[int],
    ) -> int:
        n = len(source)
        if n != len(target):
            return -1

        vocab = {}
        words = []

        def get_id(w: str) -> int:
            if w in vocab:
                return vocab[w]
            vocab[w] = len(words)
            words.append(w)
            return vocab[w]

        for a, b in zip(original, changed):
            get_id(a)
            get_id(b)

        m = len(words)
        if m == 0:
            return 0 if source == target else -1

        tmp = [dict() for _ in range(m)]
        for a, b, c in zip(original, changed, cost):
            u = vocab[a]
            v = vocab[b]
            prev = tmp[u].get(v)
            if prev is None or c < prev:
                tmp[u][v] = c

        adj = [[] for _ in range(m)]
        for u in range(m):
            for v, w in tmp[u].items():
                adj[u].append((v, w))

        INF = 10 ** 30

        dist = [[INF] * m for _ in range(m)]

        for s in range(m):
            d = dist[s]
            d[s] = 0
            pq = [(0, s)]
            while pq:
                cd, u = heapq.heappop(pq)
                if cd != d[u]:
                    continue
                for v, w in adj[u]:
                    nd = cd + w
                    if nd < d[v]:
                        d[v] = nd
                        heapq.heappush(pq, (nd, v))

        class ACNode:
            __slots__ = ("nxt", "link", "out")

            def __init__(self):
                self.nxt = {}
                self.link = 0
                self.out = []

        nodes = [ACNode()]

        def add_word(w: str, wid: int):
            cur = 0
            for ch in w:
                if ch not in nodes[cur].nxt:
                    nodes[cur].nxt[ch] = len(nodes)
                    nodes.append(ACNode())
                cur = nodes[cur].nxt[ch]
            nodes[cur].out.append(wid)

        for wid, w in enumerate(words):
            add_word(w, wid)

        q = deque()
        for ch, nx in nodes[0].nxt.items():
            nodes[nx].link = 0
            q.append(nx)

        while q:
            v = q.popleft()
            link = nodes[v].link
            if nodes[link].out:
                nodes[v].out.extend(nodes[link].out)

            for ch, nx in nodes[v].nxt.items():
                q.append(nx)
                j = nodes[v].link
                while j and ch not in nodes[j].nxt:
                    j = nodes[j].link
                nodes[nx].link = nodes[j].nxt[ch] if ch in nodes[j].nxt else 0

        lens = [len(w) for w in words]

        def occurrences_starting_at(s: str):
            starts = [[] for _ in range(len(s) + 1)]
            cur = 0
            for i, ch in enumerate(s):
                while cur and ch not in nodes[cur].nxt:
                    cur = nodes[cur].link
                if ch in nodes[cur].nxt:
                    cur = nodes[cur].nxt[ch]
                else:
                    cur = 0

                if nodes[cur].out:
                    for wid in nodes[cur].out:
                        L = lens[wid]
                        st = i - L + 1
                        if st >= 0:
                            starts[st].append((i + 1, wid))
            return starts

        src_starts = occurrences_starting_at(source)
        tgt_starts = occurrences_starting_at(target)

        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            best = INF

            if source[i] == target[i] and dp[i + 1] < best:
                best = dp[i + 1]

            if src_starts[i] and tgt_starts[i]:
                end_to_tid = {}
                for end, tid in tgt_starts[i]:
                    end_to_tid[end] = tid

                for end, sid in src_starts[i]:
                    tid = end_to_tid.get(end)
                    if tid is None:
                        continue
                    c = dist[sid][tid]
                    if c >= INF or dp[end] >= INF:
                        continue
                    val = c + dp[end]
                    if val < best:
                        best = val

            dp[i] = best

        return -1 if dp[0] >= INF else dp[0]


s = Solution()
print(s.minimumCost(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
                    changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20]))
print(s.minimumCost(source="abcdefgh", target="acdeeghh", original=["bcd", "fgh", "thh"], changed=["cde", "thh", "ghh"],
                    cost=[1, 3, 5]))
print(s.minimumCost(source="abcdefgh", target="addddddd", original=["bcd", "defgh"], changed=["ddd", "ddddd"],
                    cost=[100, 1578]))
