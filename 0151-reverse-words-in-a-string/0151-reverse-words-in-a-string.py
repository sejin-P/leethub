class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        wasBlank = True
        for letter in s:
            if letter == ' ':
                wasBlank = True
                continue
            if wasBlank:
                stack.append(letter)
            else:
                stack[-1] = stack[-1] + letter
            wasBlank = False
        
        res = ''
        while stack:
            word = stack.pop()
            res += word + ' '
        
        return res[:-1]
        