class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) >= self.k and val < self.nums[self.k-1]:
            return self.nums[self.k-1]
        
        if len(self.nums) == 0:
            self.nums.append(val)
            return val
        
        l, r = 0, min(self.k-1, len(self.nums)-1)
        
        while l < r:
            mid = (l+r) // 2
            if self.nums[mid] > val:
                l = mid+1
                continue
            if self.nums[mid] < val:
                r = mid
                continue
            break
        mid = (l+r) // 2
        
        if self.nums[mid] >= val:  
            self.nums.insert(mid+1, val)
        else:
            self.nums.insert(mid, val)
        
        return self.nums[self.k-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)