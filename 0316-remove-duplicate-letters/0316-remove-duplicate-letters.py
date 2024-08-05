from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s
        
        dup_map = defaultdict(int)
        
        for i in range(len(s)):
            dup_map[s[i]] += 1
        
        
        smallest_idx = 0
        for i in range(len(s)):
            if s[i] < s[smallest_idx]:
                smallest_idx = i
            dup_map[s[i]] -= 1
            if dup_map[s[i]] == 0:
                break
        
        return s[smallest_idx] + self.removeDuplicateLetters(s[smallest_idx:].replace(s[smallest_idx], ""))