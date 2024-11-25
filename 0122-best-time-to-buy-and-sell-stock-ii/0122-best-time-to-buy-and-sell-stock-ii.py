class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stack = []

        for price in prices:
            if stack and stack[-1] > price:
                profit += stack[-1] - stack[0]
                stack = [price]
            else:
                stack.append(price)

        if stack:
            profit += stack[-1] - stack[0]

        return profit