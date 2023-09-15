class MyHashSet:

    def __init__(self):
        self.hashpool = 0

    def add(self, key: int) -> None:
        self.hashpool |= (1 << key)
        return

    def remove(self, key: int) -> None:
        self.hashpool &= ~(1 << key)
        return

    def contains(self, key: int) -> bool:
        return bool(self.hashpool & (1 << key))


myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))
print(myHashSet.contains(3))
myHashSet.add(2)
print(myHashSet.contains(2))
myHashSet.remove(2)
print(myHashSet.contains(2))
