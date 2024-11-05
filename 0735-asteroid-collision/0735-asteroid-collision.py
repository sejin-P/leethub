class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        rightStack = []
        
        res = []
        for asteroid in asteroids:
            if asteroid > 0:
                rightStack.append(asteroid)
                continue
            
            exploded = False
            while rightStack and rightStack[-1] <= -asteroid:
                last = rightStack.pop()
                if last == -asteroid:
                    exploded = True
                    break
                
            if not exploded and not rightStack:
                res.append(asteroid)
        
        return res + rightStack
        