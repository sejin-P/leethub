class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = {}

        res = 0
        
        for num in nums:
            g = c.get(num)
            if g is not None:
                continue
            
            minus = c.get(num-1)
            plus = c.get(num+1)

            if minus is not None and plus is not None:
                c[num] = num
            elif minus is not None:
                plus = num
            elif plus is not None:
                minus = num
            else:
                plus, minus = num, num
                
            
            c[plus] = minus
            c[minus] = plus
            
            res = max(res, plus-minus+1)

        return res

            
        