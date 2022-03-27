class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        longest = s[:2] if s[0] == s[1] else s[0] 
        longest_length = len(longest)
        
        for i in range(2, len(s)):
            first_word = s[i-longest_length:i+1]
            if first_word == first_word[::-1]:
                longest = first_word
                longest_length = len(longest)
            
            if i-longest_length-1 >= 0:
                second_word = s[i-longest_length-1:i+1]
                if second_word == second_word[::-1]:
                    longest = second_word
                    longest_length = len(longest)
        
        return longest
        