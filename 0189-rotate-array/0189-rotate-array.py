class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        if k == 0:
            return
        
        r = []
    
        for i in range(k):
            r.append(nums[(i+k)%n])
            nums[(i+k)%n] = nums[i]
        
        for i in range(k, n):
            nums[(i+k)%n], r[i%k] = r[i%k], nums[(i+k)%n]
        