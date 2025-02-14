# Use the prefix products technique to make the time complexity of multiplication of k numbers after searching to O(1)
# Solve the problem of 0 encountering multiplication and division
class ProductOfNumbers:

    def __init__(self):
        self.prefix_prod_stream = [1]
        
    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_prod_stream = [1]
        else:
            self.prefix_prod_stream.append(self.prefix_prod_stream[-1]*num)
        
    def getProduct(self, k: int) -> int:
        size = len(self.prefix_prod_stream) - 1 # Exclude initial [1]
        if k > size:
            return 0
        else:
            return self.prefix_prod_stream[-1] // self.prefix_prod_stream[-(k+1)]        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
