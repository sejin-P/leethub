class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        ways = [1,2]
        for i in range(n-2):
            ways.append(ways[i] + ways[i+1])
        return ways[-1]
        