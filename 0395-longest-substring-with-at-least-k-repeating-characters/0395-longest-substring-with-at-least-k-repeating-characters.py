class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        asciia = ord('a')
        
        res = 0
        
        stringCnt = [0]*26
        for i in range(len(s)):
            stringCnt[ord(s[i]) - asciia] += 1
            if self.isValid(stringCnt, k):
                res = max(res, i+1)
                    
            copied = [stringCnt[l] for l in range(26)]
            for j in range(i):
                copied[ord(s[j]) - asciia] -= 1
                if self.isValid(copied, k):
                    res = max(res, i-j)
        
        return res
    
    def isValid(self, stringCnt, k):
        for cnt in stringCnt:
            if cnt != 0 and cnt < k:
                return False
        return True
        