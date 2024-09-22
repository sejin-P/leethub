class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.di = set(wordDict)
        self.results = set()
        self.s = s
        self.slen = len(s)
            
        return self.wbreak(0)
        
    def wbreak(self, l: int) -> bool:
        if l == self.slen:
            return True
        for i in range(l+1, self.slen+1):
            if i in self.results:
                continue
            if self.s[l:i] in self.di:
                r = self.wbreak(i)
                if r:
                    return True
                self.results.add(i)
                
        return False
        
    
    
