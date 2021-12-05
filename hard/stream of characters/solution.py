from typing import List


class StreamChecker:
    def __init__(self, words: List[str]):
        self.head = {}
        self.current = []
        for word in words:
            node = self.head
            for w in word:
                if w in node:
                    node = node[w]
                else:
                    node[w] = {}
                    node = node[w]
            node["#"] = True

    def query(self, letter: str) -> bool:
        ans = False
        temp = []
        while self.current:
            node = self.current.pop()
            if letter in node:
                temp.append(node[letter])
                if "#" in node[letter]:
                    ans = True
        if letter in self.head:
            temp.append(self.head[letter])
            if "#" in self.head[letter]:
                ans = True
        self.current = temp
        return ans


obj = StreamChecker(["cd", "f", "kl"])
print(obj.query("a"))
print(obj.query("b"))
print(obj.query("c"))
print(obj.query("d"))
print(obj.query("e"))
print(obj.query("f"))
print(obj.query("g"))
print(obj.query("h"))
print(obj.query("i"))
print(obj.query("j"))
print(obj.query("k"))
print(obj.query("l"))
