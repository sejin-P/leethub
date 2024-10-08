class Solution:
    def __init__(self):
        self.digit_map = {"2": ["a", "b", "c"],
                          "3": ["d", "e", "f"],
                         "4": ["g", "h", "i"],
                         "5": ["j", "k", "l"],
                         "6": ["m", "n", "o"],
                         "7": ["p", "q", "r", "s"],
                         "8": ["t", "u", "v"],
                         "9": ["w", "x", "y", "z"]}
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.digit_map[digits[0]]
        
        posts = self.letterCombinations(digits[1:])
        res = []
        for s in self.digit_map[digits[0]]:
            for post in posts:
                res.append(s+post)
            
        return res
        