class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        endMap = {}
        
        maxLen = 0
        for num in nums:
            if num in endMap:
                continue
            
            lessEnd = endMap.get(num-1)
            moreEnd = endMap.get(num+1)
            if lessEnd is not None and moreEnd is not None:
                endMap[lessEnd] = moreEnd
                endMap[moreEnd] = lessEnd
                endMap[num] = num
                maxLen = max(maxLen, moreEnd-lessEnd+1)
            elif lessEnd is not None:
                endMap[lessEnd] = num
                endMap[num] = lessEnd
                maxLen = max(maxLen, num-lessEnd+1)
            elif moreEnd is not None:
                endMap[moreEnd] = num
                endMap[num] = moreEnd
                maxLen = max(maxLen, moreEnd-num+1)
            else:
                endMap[num] = num
                maxLen = max(maxLen, 1)
        
        return maxLen
        