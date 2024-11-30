class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        word = ''
        wasBlank = True
        for letter in s:
            if letter == ' ':
                if word:
                    res = word + ' ' + res
                    word = ''
                wasBlank = True
                continue
            word += letter
            wasBlank = False
        
        if word:
            res = word + ' ' + res
        
        return res[:-1]
        