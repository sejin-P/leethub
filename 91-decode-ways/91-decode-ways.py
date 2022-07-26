class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        
        results = [1]+[0]*(len(s)-1)
        num2 = int(s[:2])
        if (num2 >= 11 and num2 <= 19) or (num2 >= 21 and num2 <= 26):
            results[1] = 2
        elif num2 == 10 or num2 == 20:
            results[1] = 1
        elif s[0] != "0" and s[1] != "0":
            results[1] = 1
        else:
            return 0
        
        for i in range(2, len(s)):
            if s[i] != "0":
                if s[i-1] == "1":
                    results[i] = results[i-1] + results[i-2]
                elif s[i-1] == "2":
                    if s[i] in ["1", "2", "3", "4", "5", "6"]:
                        results[i] = results[i-1] + results[i-2]
                    else:
                        results[i] = results[i-1]
                else:
                    results[i] = results[i-1]
            else:
                if s[i-1] == "1" or s[i-1] == "2":
                    results[i] = results[i-2]
                else:
                    return 0
        
        return results[-1]
        