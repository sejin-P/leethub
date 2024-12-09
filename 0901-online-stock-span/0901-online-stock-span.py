class StockSpanner:

    def __init__(self):
        self.stocks = []
        

    def next(self, price: int) -> int:
        res = 1
        while self.stocks and self.stocks[-1][0] <= price:
            popped = self.stocks.pop()
            res += popped[1]
            
        self.stocks.append((price, res))
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)