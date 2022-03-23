class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_dict = {}
        result = 0
        start = 0
        for i in range(len(s)):
            idx = letter_dict.get(s[i])
            if idx is None or idx < start:
                if i - start + 1 > result:
                    result = i - start + 1
            else:
                start = idx + 1
            letter_dict[s[i]] = i
        
        return result
            