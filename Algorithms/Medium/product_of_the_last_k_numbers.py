# https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:

    def __init__(self):
        self.product = [1]
        self.max_zero_idx = -1

    def add(self, num):
        if num == 0:
            self.product.append(self.product[-1] * 1)
            self.max_zero_idx = len(self.product) - 1
        else:
            self.product.append(self.product[-1] * num)
            
    def getProduct(self, k):
        N = len(self.product)
        if self.max_zero_idx <= N - 1 - k:
            return self.product[-1] // self.product[-1-k]
        else:
            return 0
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
