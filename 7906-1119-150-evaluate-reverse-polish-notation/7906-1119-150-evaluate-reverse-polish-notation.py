class Solution:
    def __init__(self):
        self.divide = "/"
        self.plus = "+"
        self.minus = "-"
        self.multiply = "*"
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == self.divide:
                after = stack.pop()
                before = stack.pop()
                n = before // after
                if n < 0 and before%after != 0:
                    stack.append(n+1)
                else:
                    stack.append(n)
            elif token == self.plus:
                after = stack.pop()
                before = stack.pop()
                stack.append(before + after)
            elif token == self.minus:
                after = stack.pop()
                before = stack.pop()
                stack.append(before - after)
            elif token == self.multiply:
                after = stack.pop()
                before = stack.pop()
                stack.append(after*before)
            else:
                stack.append(int(token))

        return stack[0]
        