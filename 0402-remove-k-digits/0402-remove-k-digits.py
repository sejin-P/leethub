class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        
        for digit in num:
            while s and s[-1] > digit and k > 0:
                s.pop()
                k -= 1
            s.append(digit)
            
        if k > 0:
            s = s[:len(s)-k]
        
        res = ""
        wasZero = True
        for i in range(len(s)):
            if wasZero and s[i] == "0":
                continue
            wasZero = False
            res += s[i]
        
        return res if res else "0"
            
            
        