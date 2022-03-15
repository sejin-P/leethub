class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        q = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                q.append(bracket)
            else:
                if len(q) == 0 or q.pop() != bracket_map[bracket]:
                    return False
        if len(q) > 0:
            return False
        return True
    