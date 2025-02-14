class ProductOfNumbers:
    def __init__(self):
        self.product = 1
        self.product_list = []

    def add(self, num: int) -> None:
        if num == 0:
            self.product = 1
            self.product_list = []
        else:
            self.product *= num
            self.product_list.append(self.product)

    def getProduct(self, k: int) -> int:
        n = len(self.product_list)
        if n < k:
            return 0
        last = self.product_list[-1]
        if n == k:
            return last
        return last // self.product_list[-k - 1]


p = ProductOfNumbers()
p.add(3)
p.add(0)
p.add(2)
p.add(5)
p.add(4)
print(p.getProduct(2))
print(p.getProduct(3))
print(p.getProduct(4))
p.add(8)
print(p.getProduct(2))
