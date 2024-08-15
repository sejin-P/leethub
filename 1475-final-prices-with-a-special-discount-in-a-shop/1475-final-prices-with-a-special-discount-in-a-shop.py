class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        res = [0]*n
        for i in range(n):
            res[i] = prices[i]
            while stack and prices[stack[-1]] >= prices[i]:
                prev = stack.pop()
                res[prev] = res[prev] - prices[i]
            stack.append(i)
        return res
        