class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        curr = 0
        n = len(gas)
        answer = 0
        
        for i in range(n):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                answer = i+1
        
        return answer if total >= 0 else -1
            
        