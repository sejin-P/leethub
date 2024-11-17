from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        asciia = ord('a')
        stringCounter = Counter(s)
        
        maxUnique = len(stringCounter.keys())
        res = 0
        
        for currUnique in range(1, maxUnique+1):
            start, end = 0, 0
            unique, countAtLeastK = 0, 0
            stringCnt = [0]*26
            
            while end < len(s):
                if unique <= currUnique:
                    order = ord(s[end]) - asciia
                    if stringCnt[order] == 0:
                        unique += 1
                    stringCnt[order] += 1
                    if stringCnt[order] == k:
                        countAtLeastK += 1
                    end += 1
                else:
                    order = ord(s[start]) - asciia
                    if stringCnt[order] == 1:
                        unique -= 1
                    stringCnt[order] -= 1
                    if stringCnt[order] == k-1:
                        countAtLeastK -= 1
                    start += 1
                if (unique == currUnique) and (unique == countAtLeastK):
                    res = max(res, end-start)
        
        return res
        
        