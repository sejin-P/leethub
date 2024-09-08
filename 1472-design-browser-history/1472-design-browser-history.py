class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history = []
        self.cursor = -1
        

    def visit(self, url: str) -> None:
        self.cursor += 1
        
        for i in range(self.cursor, len(self.history)):
            self.history.pop()
            
        self.history.append(url)
        

    def back(self, steps: int) -> str:
        if steps > self.cursor:
            self.cursor = -1
            return self.homepage
        
        self.cursor -= steps
        return self.history[self.cursor]
        

    def forward(self, steps: int) -> str:
        self.cursor = min(self.cursor+steps, len(self.history)-1)
        if self.cursor == -1:
            return self.homepage
        return self.history[self.cursor]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)