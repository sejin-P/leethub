class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k:
            return n
        
        left, right = 0, 0
        h = {}
        
        maxLen = 0
        while right < n:
            h[s[right]] = right
            
            if len(h) == k+1:
                maxLen = max(maxLen, right-left)
                delIdx = min(h.values())
                left = delIdx+1
                del h[s[delIdx]]
        
            right += 1
    
        return max(maxLen, right-left)