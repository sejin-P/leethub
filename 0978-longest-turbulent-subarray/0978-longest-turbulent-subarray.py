class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        if n == 2:
            if arr[0] == arr[1]:
                return 1
            return 2
        maxLen = 1 if arr[0] == arr[1] else 2
        left, right = 0, 2
        while right < n:
            if arr[right-2] < arr[right-1] and arr[right-1] > arr[right]:
                maxLen = max(right-left+1, maxLen)
            elif arr[right-2] > arr[right-1] and arr[right-1] < arr[right]:
                maxLen = max(right-left+1, maxLen)
            else:
                if arr[right-1] != arr[right]:
                    maxLen = max(maxLen, 2)
                left = right - 1
            
            right += 1
            
        return maxLen
            
        