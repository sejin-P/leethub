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
            n_idx = (i+k)%n
            r_idx = i%k
            nums[n_idx], r[r_idx] = r[r_idx], nums[n_idx]
        