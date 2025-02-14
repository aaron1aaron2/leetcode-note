# The basic solution, where getProduct() is O(k). Python will timeout, but C++ implementation will not
class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        

    def add(self, num: int) -> None:
        self.stream.append(num)

    def getProduct(self, k: int) -> int:
        result = 1
        for i in self.stream[-k:]:
            result *= i

        return result
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
