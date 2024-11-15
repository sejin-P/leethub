from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        
        for num in nums:
            cnt[num] += 1
            
        minVal = len(nums)
        maxVal = 0
        
        valDict = defaultdict(list)
        for key in cnt.keys():
            val = cnt[key]
            valDict[val].append(key)
            if val <= minVal:
                minVal = val
            if maxVal <= val:
                maxVal = val
        
        field = [0]*(maxVal-minVal+1)
        
        for key in cnt.keys():
            field[cnt[key]-minVal] += 1
        
        res = []
        for idx in range(len(field)-1, -1, -1):
            valCnt = field[idx]
            if valCnt == 0:
                continue
            
            k -= valCnt
            res += valDict[minVal+idx]
            
            if k <= 0:
                return res
        