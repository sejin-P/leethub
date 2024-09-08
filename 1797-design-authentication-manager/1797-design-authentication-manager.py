from collections import OrderedDict

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = OrderedDict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl
    
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.ttl
            self.tokens.move_to_end(tokenId, last = True)
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.tokens:
            d = False
            for key in self.tokens.keys():
                if self.tokens[key] <= currentTime:
                    d = True
                    break
            if d:
                self.tokens.popitem(last=False)
                continue
            break
        return len(self.tokens)
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)